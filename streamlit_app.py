import streamlit as st
import pandas as pd
st.title('📈Marketing Campaign Analysis')

st.info('This app calculates impact of Marketing Campaign Analysis on sales and customer behaviour.')

df = pd.read_csv('https://raw.githubusercontent.com/Divy-Parekh/mlproject/refs/heads/master/marketing_campaign_dataset.csv')
df
