import streamlit as st
import pandas as pd
import time
import plotly.express as px
import glob
import os 

# sensors_csv = 'sensors_csv.csv'
path_to_csv = glob.glob('*.csv')
sensors_csv = glob.glob(max(path_to_csv, key=os.path.getctime))[0]

# creating individual plots for each sensor
def plotly(sensors_df, sensor_number):
    y = sensor_number
    sensors_df1 = sensors_df.tail(30)
    plot = px.line(sensors_df1, x='TIMESTAMP', y=y)
    st.plotly_chart(plot, use_container_width=True, theme='streamlit')

# creating one plot including all sensors
def plotly_all(sensors_df):
    sensors_df2 = sensors_df.drop(columns='is_motion').tail(30)
    sensors_df3 = sensors_df2.dropna()
    st.line_chart(data=sensors_df3, x='TIMESTAMP')

# converting the sensors_df into CSV
@st.cache_data
def convert_sensors_df(sensors_df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return sensors_df.to_csv().encode('utf-8')

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
Sensor1, Sensor2, Sensor3, Sensor4 = st.columns(4)
sensors_df = pd.read_csv((sensors_csv))
sensors_df2 = sensors_df.drop(columns='is_motion').tail(30)
sensors_df3 = sensors_df2.dropna()
try:
    st.write(sensors_df)
    st.write(sensors_df2)
    st.write(sensors_df3)
except: 
    st.write(sensors_df3)
Sensor1.metric(
    
    label="Sensor 1 RH",
    value=sensors_df3['Sensor 1'].iloc[-1]
)
Sensor2.metric(
    
    label="Sensor 2 RH",
    value=sensors_df3['Sensor 2'].iloc[-1]
)
Sensor3.metric(
    
    label="Sensor 3 RH",
    value=sensors_df3['Sensor 3'].iloc[-1]
)
Sensor4.metric(
    
    label="Sensor 4 RH",
    value=sensors_df3['Sensor 4'].iloc[-1]
)


# plotting all sensors into one plot
plotly_all(sensors_df)

placeholder = st.empty()
if sensors_df['is_motion'].iloc[-1] == 1:
    # placeholder.markdown('**:red[Motion Detected - Alarm is ACTIVE]**')
    placeholder.text('dfdfdfdf')
    # st.markdown('**:red[Motion Detected - Alarm is ACTIVE]**')

else:
    placeholder.markdown('**:green[No Motion Detected - No Alarm]**')
    # st.markdown('**:green[No Motion Detected - No Alarm]**')
placeholder.empty()

# creating the download button
csv = convert_sensors_df(sensors_df)
st.download_button(
    label="Download last data as CSV",
    data=csv,
    file_name='Sensors_Data.csv',
    mime='text/csv',
)

if st.button(label='HighTech Computing Integration Module'):
    st.snow()

col1, col2 = st.columns(2)
sensors_df = pd.read_csv(sensors_csv)

with col1:
    label='graph'
    value=plotly(sensors_df3, 'Sensor 1')
with col2:
    label='grapg'
    value=plotly(sensors_df3, 'Sensor 2')

col1, col2 = st.columns(2)

with col1:
    label='graph'
    value=plotly(sensors_df3, 'Sensor 3')
with col2:
    label='graph'
    value=plotly(sensors_df3, 'Sensor 4')


time.sleep(1)