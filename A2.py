import streamlit as st
import pandas as pd 
import csv
st.title('avaliação do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('preço_notebooks_excel.xlsx', sep =';')
st.dataframe(df)

#arquivo = open('preço_notebooks_excel.xlsx')
#for linha in arquivo:
#    st.write(linha)
