import streamlit as st
import pandas as pd 
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('acidentes.csv', sep =',')
st.dataframe(df)
