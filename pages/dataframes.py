import streamlit as st
from dataset import df

st.title("Datast de Vendas")

with st.expander("Colunas"):
    colunas = st.multiselect(
        'selecione as colunas',
        list(df.columns),
        list(df.columns)
        )
    
st.sidebar.title("Filtros")
with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect(
        'selecione as categorias',
        list(df['Categoria do Produto'].unique()),
        list(df['Categoria do Produto'].unique())
    )

with st.sidebar.expander("Preço"):
    preco = st.slider(
        'Selecione o intervalo de preço',
        float(df['Preço'].min()),
        float(df['Preço'].max()),
        (float(df['Preço'].min()), float(df['Preço'].max()))
    )
    
with st.sidebar.expander("Data da Compra"):
    data_compra = st.date_input(
        'Selecione o intervalo de data',
        (df['Data da Compra'].min(),
         df['Data da Compra'].max())
    )
    

st.dataframe(df)
