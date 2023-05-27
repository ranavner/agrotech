import streamlit as st
import pandas as pd
import time
import plotly.express as px

# creating individual plots for each sensor
def plotly(df, sensor_number):
    y = sensor_number
    df1 = df.tail(30)
    plot = px.line(df1, x='TIMESTAMP', y=y)
    st.plotly_chart(plot, use_container_width=True, theme='streamlit')

# creating one plot including all sensors
def plotly_all(df):
    df1 = df.tail(30)
    st.line_chart(data=df1, x='TIMESTAMP')

# converting the df into CSV
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def create_snow():
    st.snow

# streamllit configuration
st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Agrotech Project Dashboard")

# first appearance - sensors current measurments
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

# plotting all sensors into one plot
plotly_all(df)

# creating the download button
csv = convert_df(df)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Sensors_Data.csv',
    mime='text/csv',
)

if st.button(label='HighTech Computing Integration Module Unit'):
    st.snow()

col1, col2, col3 = st.columns(3)
df = pd.read_csv('fixed2.csv')

with col1:
    label='graph'
    value=plotly(df, 'sensor1')
with col2:
    label='grapg'
    value=plotly(df, 'sensor2')
with col3:
    label='graph'
    value=plotly(df, 'sensor3')

col1, col2, col3 = st.columns(3)

with col1:
    label='graph'
    value=plotly(df, 'sensor4')
with col2:
    label='graph'
    value=plotly(df, 'sensor5')
with col3:
    label='graph'
    value=plotly(df, 'sensor6')


time.sleep(1)