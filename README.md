# 🐥Twitter (X) Sentiment Dashboard

> Um painel interativo para analisar sentimentos expressos em posts no X em tempo real, útil para gerar uma visão de como um assunto ou marca é visualizado ou sentido por um público.

## 📌 Funcionalidades

- Coleta de tweets em tempo real com base em uma palavra-chave.
- Classificação dos sentimentos (Positivo, Negativo ou Neutro).
- Visualização gráfica da distribuição de sentimentos.
- Interface interativa e fácil de usar com Streamlit.

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

- Python 3.10 ou superior
- Conta no X (antigo Twitter) com permissões para a API v2

### 2. Clone o repositório

```
git clone https://github.com/seu-usuario/twitter-sentiment-dashboard.git
cd twitter-sentiment-dashboard
```

### 3. Crie seu ambiente virtual
```
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

### 4. Instale as dependências
```
pip install -r requirements.txt
```

### 5.  Configure a credencia BEARER_TOKEN no seu arquivo .env
```
BEARER_TOKEN="seu-token-aki"
```

### 6. Execute o dashboard

```
streamlit run app.py
```
## Exemplo de uso

1. Insira a palavra chave no campo de pesquisa
2. Ajuste a quantidade de tweets para análise (0 a 100)
3. Clique em analisar tweets para gerar resultados.


## 🛠️ Tecnologias Utilizadas
Python: Linguagem principal do projeto
Streamlit: Interface interativa
Tweepy: Acesso à API do Twitter
TextBlob: Análise de sentimento
dotenv: Gerenciamento seguro de variáveis sensíveis


##🗝 Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.

