import streamlit as st
import pandas as pd 
import csv
st.title('avaliação do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('preço_notebooks.csv', sep =';')
st.dataframe(df)

#arquivo = open('preço_notebooks.csv')
#for linha in arquivo:
#    st.write(linha)
