#!/usr/bin/env python
# coding: utf-8


# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


# In[2]:

st.set_page_config(page_title='Youtube Comments Filter')

image= Image.open('/Users/harshavarthanan/Downloads/Excel_Webapp/youtube.png')
st.image(image, use_column_width=True)


st.header('Youtube Comment Filter - Avatar 2 Trailer')

image= Image.open('/Users/harshavarthanan/Downloads/Excel_Webapp/avatar-2-the-way-of-water.jpg')
st.image(image, use_column_width=True)
st.subheader('Filter by Topics & Sentiment')

### --- LOAD DATAFRAME
excel_file = '/Users/harshavarthanan/Downloads/Excel_Webapp/webappin.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:C',
                   header=0)

topic = df['Topic'].unique().tolist()

topic_selection = st.multiselect('Topic',topic,default=None)

mask1 = (df['Topic'].isin(topic_selection))
number_of_result1 = df[mask1].shape[0]

st.markdown(f'*Available Results: {number_of_result1}*')

sentiment = df['Sentiment'].unique().tolist()

sentiment_selection = st.multiselect('Sentiment',sentiment,default=None)


mask2 = (df['Sentiment'].isin(sentiment_selection))
number_of_result2 = df[mask2].shape[0]

st.markdown(f'*Available Results: {number_of_result2}*')


if number_of_result1 == 0 and number_of_result2 == 0:
    st.dataframe(df['Comment'])
elif number_of_result1 != 0 and number_of_result2 == 0:
    st.dataframe(df['Comment'][mask1])
elif number_of_result1 == 0 and number_of_result2 != 0:
    st.dataframe(df['Comment'][mask2])
elif number_of_result1 != 0 and number_of_result2 != 0:
    st.dataframe(df['Comment'][mask1][mask2])
    
    












