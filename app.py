# app.py
import streamlit as st
import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações da API do Twitter
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Autenticação na API do Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Função para analisar sentimento
def analisar_sentimento(texto):
    analise = TextBlob(texto)
    if analise.sentiment.polarity > 0:
        return "Positivo"
    elif analise.sentiment.polarity < 0:
        return "Negativo"
    else:
        return "Neutro"

# Função para buscar tweets (API v2)
def buscar_tweets(termo, quantidade=100):
    resposta = client.search_recent_tweets(query=termo, max_results=quantidade, tweet_fields=["author_id", "text"])
    tweets = resposta.data
    if not tweets:
        return pd.DataFrame(columns=["Usuário", "Tweet", "Sentimento"])

    dados = [(tweet.author_id, tweet.text, analisar_sentimento(tweet.text)) for tweet in tweets]
    return pd.DataFrame(dados, columns=["Usuário", "Tweet", "Sentimento"])

# Interface do Dashboard
st.title("Monitoramento de Redes Sociais")

termo = st.text_input("Insira a palavra-chave para monitorar:", "suaMarca")
quantidade = st.slider("Número de tweets a coletar:", 10, 100, 50)

if st.button("Analisar Tweets"):
    df = buscar_tweets(termo, quantidade)
    if df.empty:
        st.warning("Nenhum tweet encontrado para o termo informado.")
    else:
        st.write(df)

        # Gráfico de Sentimento
        st.subheader("Distribuição de Sentimentos")
        fig, ax = plt.subplots()
        df["Sentimento"].value_counts().plot(kind="bar", ax=ax, color=["green", "red", "gray"])
        st.pyplot(fig)

        st.success("Análise concluída com sucesso!")
