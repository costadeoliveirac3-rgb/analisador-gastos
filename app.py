import pandas as pd 
import plotly.express as px 
import streamlit as st

st.title('Analisador de Gastos Pessoais')
st.markdown('Faça um uploud do seu extrato em CSV  e veja seus gastos organizados.')

arquivo = st.file_uploader('Envie seu extrato CSV', type ='csv')

if arquivo is not None:
    df = pd.read_csv(arquivo, skipinitialspace=True)

    st.subheader('Resumo do mês')
    col1, col2, col3 = st.columns(3)
    col1.metric('Total gasto', f'R$ {df['valor'].sum():.2f}')
    col2.metric('Maior gasto do mês', f'R${df['valor'].max():.2f}')
    col3.metric('Menor gasto do mês', f'R$ {df['valor'].min():.2f}')

    st.subheader('Gastos por categoria')
    por_categoria = df.groupby('categoria')['valor'].sum().reset_index()
    fig1 = px.pie(por_categoria, values='valor', names='categoria', hole=0.4)
    st.plotly_chart(fig1)

    st.subheader('Evolução gastos no mês')
    df['data'] = pd.to_datetime(df['data'])
    df = df.sort_values('data')
    fig2 = px.line(df, x='data', y='valor', color='categoria', markers=True)
    st.plotly_chart(fig2)

    st.subheader('Todos os lançamentos')
    st.dataframe(df)




