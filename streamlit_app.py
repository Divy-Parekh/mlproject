import streamlit as st
import pandas as pd
st.title('📈Marketing Campaign Analysis')

st.info('This app calculates impact of Marketing Campaign Analysis on sales and customer behaviour.')


with st.expander('Data'):
  st.write('**Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/Divy-Parekh/mlproject/refs/heads/master/marketing_campaign_dataset.csv')
  df


with st.expander('Data Visualization'):
  avg_roi_by_campaign_type = df.groupby(['Campaign_Type'])['ROI'].mean()
  st.bar_chart(data=df,x='Campaign_Type',y='ROI')
  



