# 📊 Analisador de Gastos Pessoais

Dashboard interativo para análise de gastos pessoais a partir de extratos bancários em CSV.

## 🔗 Acesse o projeto
(https://costadeoliveirac3-rgb-analisador-gastos-app-elt4nm.streamlit.app/)

## 💡 O que o projeto faz
- Faz upload do extrato bancário em CSV
- Calcula total gasto, maior e menor gasto do mês
- Gera gráfico de pizza com gastos por categoria
- Gera gráfico de linha com evolução dos gastos no mês
- Exibe tabela completa dos lançamentos

## 🛠️ Tecnologias usadas
- Python
- Pandas
- Streamlit
- Plotly

## ▶️ Como rodar localmente
```bash
# Clone o repositório
git clone https://github.com/costadeoliveirac3-rgb/analisador-gastos.git

# Entre na pasta
cd analisador-gastos

# Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o projeto
streamlit run app.py
```

## 👤 Autor
Carlos Henrique — Estudante de Engenharia de Software 