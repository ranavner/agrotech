import streamlit as st
import pandas as pd
import time
import plotly.express as px
import glob
import os 
import gdown
from PIL import Image
from PIL import ImageOps

# sensors_csv = 'sensors_csv.csv'
path_to_csv = glob.glob('*.csv')
sensors_csv = glob.glob(max(path_to_csv, key=os.path.getctime))[0]

path_to_image_directory = glob.glob('ESP32-CAM/*')
latest_image_directory = glob.glob(max(path_to_image_directory, key=os.path.getctime))[0]
path_to_image = glob.glob(latest_image_directory + '/*')
image_now = glob.glob(max(path_to_image, key=os.path.getctime))[0]

def download_from_drive():
    url = "https://drive.google.com/drive/folders/1Ct5QfEFchW4f0ejEFRlJ4ahySA_rOqvj?usp=sharing"
    gdown.download_folder(url, quiet=True, use_cookies=False)

def main():

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
    
    placeholder1 = st.columns(4)
    Sensor1 = placeholder1[0].empty()
    Sensor2 = placeholder1[1].empty()
    Sensor3 = placeholder1[2].empty()
    Sensor4 = placeholder1[3].empty()

    placeholder2 = st.columns(2)
    tmp = placeholder2[0].empty()
    VPD = placeholder2[1].empty()

    placeholder_motion = st.empty()
    is_motion = placeholder_motion

    placeholder3 = st.empty()
    data_4_table = placeholder3

    placeholder4 = st.empty()
    all_sensors_plot = placeholder4

    placeholder5 = st.columns(2)
    tmp_graph = placeholder5[0].empty()
    VPD_graph = placeholder5[1].empty()

    placeholder_image = st.empty()
    image = placeholder_image

    def update_displayed_data(sensors_df4):
        Sensor1.metric(
            
            label="Sensor 1 RH",
            value=sensors_df4['Sensor 1'].iloc[-1]
        )
        Sensor2.metric(
            
            label="Sensor 2 RH",
            value=sensors_df4['Sensor 2'].iloc[-1]
        )
        Sensor3.metric(
            
            label="Sensor 3 RH",
            value=sensors_df4['Sensor 3'].iloc[-1]
        )
        Sensor4.metric(
            
            label="Sensor 4 RH",
            value=sensors_df4['Sensor 4'].iloc[-1]
        )

        tmp.metric(

            label='Field Temperture',
            value=sensors_df4['tmp'].iloc[-1]
        )
        VPD.metric(

            label='Field VPD',
            value=sensors_df4['vpd'].iloc[-1]
        )

        if sensors_df['is_motion'].iloc[-1] == 1:
            is_motion.markdown('**:red[Motion Detected - Alarm is ACTIVE]**')
            # st.markdown('**:red[Motion Detected - Alarm is ACTIVE]**')

        else:
            is_motion.markdown('**:green[No Motion Detected - No Alarm]**')
            # st.markdown('**:green[No Motion Detected - No Alarm]**')

        data_4_table.write(sensors_df4)
        all_sensors_plot.line_chart(data=sensors_df5, x='TIMESTAMP')
        
        tmp_graph.line_chart(sensors_df4, x='TIMESTAMP', y='tmp')
        VPD_graph.line_chart(sensors_df4, x='TIMESTAMP', y='vpd')

        image.image(image_now, width=720)

        # add buttons:

# ---------------------------------------------------------- until here, synced with GUI_test.py

    while True:
        # st.image(image)
        sensors_df = pd.read_csv((sensors_csv))
        sensors_df2 = sensors_df.drop(columns=['is_motion'])
        sensors_df3 = sensors_df2.dropna()
        sensors_df4 = sensors_df3.sort_values('TIMESTAMP').drop_duplicates(keep='last')
        sensors_df4 = sensors_df4.tail(30)
        sensors_df5 = sensors_df4.drop(columns=['tmp', 'vpd'])
        motion_df = sensors_df.drop(columns=['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'tmp', 'vpd'])
        update_displayed_data(sensors_df4)
        time.sleep(1)

    Sensor1.empty()
    Sensor2.empty()
    Sensor3.empty()
    Sensor4.empty()

try:
    download_from_drive()
    main()
except:
    st.image('waiting_image.jpg', use_column_width=False)
    st.title("GATHERING DATA, PLEASE WAIT...")