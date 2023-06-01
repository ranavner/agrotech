import streamlit as st
import pandas as pd
import time
import glob
import os.path

path_to_csv = glob.glob('*.csv')
sensors_csv = glob.glob(max(path_to_csv, key=os.path.getctime))[0]

sensors_df = pd.read_csv('sensors_csv_2023-05-30 15:52:57.768643.csv')
sensors_df2 = sensors_df.drop(columns=['is_motion', 'tmp', 'vpd'])
sensors_df3 = sensors_df2.dropna()
sensors_df4 = sensors_df3.sort_values('TIMESTAMP').drop_duplicates(keep='last')
sensors_df4 = sensors_df4.tail(30)

st.write('Initial dataframe')
st.write(sensors_df4)

placeholder = st.columns(4)
Sensor1 = placeholder[0].empty()
Sensor2 = placeholder[1].empty()
Sensor3 = placeholder[2].empty()
Sensor4 = placeholder[3].empty()

def update_displayed_metric(df):
    Sensor1.metric(
        label="Sensor 1 RH",
        value=df['Sensor 1'].iloc[-1]
    )
    Sensor2.metric(
        
        label="Sensor 2 RH",
        value=df['Sensor 2'].iloc[-1]
    )
    Sensor3.metric(
        
        label="Sensor 3 RH",
        value=df['Sensor 3'].iloc[-1]
    )
    Sensor4.metric(
        
        label="Sensor 4 RH",
        value=df['Sensor 4'].iloc[-1]
    )
def update_sensor_values(df):
    df['Sensor 1'] = 1



i = 0
while i < 10:
    
    update_displayed_metric(sensors_df4)
    df = update_sensor_values(sensors_df4)
    time.sleep(1)
    i += 1

Sensor1.empty()
Sensor2.empty()
Sensor3.empty()
Sensor4.empty()