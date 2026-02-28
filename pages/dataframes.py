import streamlit as st
from dataset import df
from utils import convert_csv , mensagem_sucesso

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

query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= `Preço` <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)

st.markdown(f"A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas")

st.markdown('Escreva um nome do arquivo para download')

coluna1 , coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility = 'collapsed'
    )
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )
