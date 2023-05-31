import streamlit as st
import pandas as pd 
import csv
st.title('trabalho csv')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('Human.csv', sep =',')
st.dataframe(df)
