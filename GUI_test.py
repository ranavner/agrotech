import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Agrotech Project Dashboard")

Sensor1, Sensor2, Sensor3, Sensor4, Sensor5, Sensor6 = st.columns(6)
df = pd.read_csv(('fixed2.csv'))
Sensor1.metric(
    
    label="Sensor 1 RH",
    value=df['sensor1'].iloc[-1]
)
Sensor2.metric(
    
    label="Sensor 2 RH",
    value=df['sensor2'].iloc[-1]
)
Sensor3.metric(
    
    label="Sensor 3 RH",
    value=df['sensor3'].iloc[-1]
)
Sensor4.metric(
    
    label="Sensor 4 RH",
    value=df['sensor4'].iloc[-1]
)
Sensor5.metric(
    
    label="Sensor 5 RH",
    value=df['sensor5'].iloc[-1]
)
Sensor6.metric(
    
    label="Sensor 6 RH",
    value=df['sensor6'].iloc[-1]
)

col1, col2 = st.columns(2)
df = pd.read_csv('fixed2.csv')

with col1:
    label='graph'
    value=st.line_chart(df)
with col2:
    label='table'
    value=st.write(df)

time.sleep(1)