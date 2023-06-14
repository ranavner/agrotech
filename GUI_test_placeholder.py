import streamlit as st
import pandas as pd
import time
import plotly.express as px
import glob
import os
import base64

path_to_csv = glob.glob('*.csv')
sensors_csv = glob.glob(max(path_to_csv, key=os.path.getctime))[0]
#   _______________________________________________________________________________________________________

try:
    path_to_image_directory = glob.glob('ESP32-CAM/*')
    latest_image_directory = glob.glob(max(path_to_image_directory, key=os.path.getctime))[0]
    path_to_image = glob.glob(latest_image_directory + '/*')
    image_now = glob.glob(max(path_to_image, key=os.path.getctime))[0]
except:
    pass
#   _______________________________________________________________________________________________________

@st.cache_data
def convert_sensors_df(sensors_df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return sensors_df.to_csv().encode('utf-8')

# defining background image
def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

# defining background image
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#   _______________________________________________________________________________________________________

def main():

    # converting the sensors_df into CSV
    @st.cache_data
    def convert_sensors_df(sensors_df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return sensors_df.to_csv().encode('utf-8')

    # streamllit page configuration
    st.set_page_config(
        page_title="Real-Time-Field Dashboard",
        page_icon="💧",
        layout="wide",
    )
    # calling the background image function (insert .png file path)
    set_background('Background.png')

    st.title("💧 Real-Data-Field Dashboard")

#   _____________________________________PLACE HOLDERS___________________________________________________

    # first appearance - sensors current measurments
    Sensor1, Sensor2, Sensor3, Sensor4 = st.columns(4)
    
    placeholder1 = st.columns(4)
    Sensor1 = placeholder1[0].empty()
    Sensor2 = placeholder1[1].empty()
    Sensor3 = placeholder1[2].empty()
    Sensor4 = placeholder1[3].empty()

    # valve_status appearance
    valve1, valve2, valve3, valve4 = st.columns(4)
    
    valve_placeholder = st.columns(4)
    valve1 = valve_placeholder[0].empty()
    valve2 = valve_placeholder[1].empty()
    valve3 = valve_placeholder[2].empty()
    valve4 = valve_placeholder[3].empty()

    # tmp and VPD data
    placeholder2 = st.columns(2)

    tmp = placeholder2[0].empty()
    VPD = placeholder2[1].empty()

    # motion sensor status
    placeholder_motion = st.empty()
    is_motion = placeholder_motion
    # motion sensor last detection
    place_holder_last_seen = st.empty()
    last_seen = place_holder_last_seen

    # tmp table
    placeholder3 = st.empty()
    data_4_table = placeholder3

    # plotting all sensors in one graph
    placeholder4 = st.empty()
    all_sensors_plot = placeholder4

    # plotting the tmp and the VPD
    placeholder5 = st.columns(2)

    tmp_graph = placeholder5[0].empty()
    VPD_graph = placeholder5[1].empty()

    # presenting the image from the ESP32 cam module (downloaded from drive)
    placeholder_image = st.empty()
    image = placeholder_image

    # creating the csv download button
    csv = convert_sensors_df(sensors_df)
    st.download_button(
        label="Download RAW as CSV",
        data=csv,
        file_name='Sensors_Data.csv',
        mime='text/csv',
    )
#   ____________________________________POSITIONING_________________________________________________________

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

        valve1.metric(
            
            label="Valve 1 Status",
            value=sensors_df4['Sensor 1'].iloc[-1]
        )
        valve2.metric(
            
            label="Valve 2 Status",
            value=sensors_df4['Sensor 2'].iloc[-1]
        )
        valve3.metric(
            
            label="Valve 3 Status",
            value=sensors_df4['Sensor 3'].iloc[-1]
        )
        valve4.metric(
            
            label="Valve 4 Status",
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

        else:
            is_motion.markdown('**:green[No Motion Detected - No Alarm]**')
            last_seen.markdown("Last Motion: " + motion_last_seen)

        data_4_table.write(sensors_df4)
        all_sensors_plot.line_chart(data=sensors_df5, x='TIMESTAMP')
        
        tmp_graph.line_chart(sensors_df4, x='TIMESTAMP', y='tmp')
        VPD_graph.line_chart(sensors_df4, x='TIMESTAMP', y='vpd')

        image.image(image_now, width=720)

        # add buttons:

#   _______________________________________________________________________________________________________

    def define_data_frames():
        global sensors_df, sensors_df2, sensors_df3, sensors_df4, sensors_df5, motion_df, motion_last_seen
        sensors_df = pd.read_csv((sensors_csv))
        sensors_df2 = sensors_df.drop(columns=['is_motion'])
        sensors_df3 = sensors_df2.dropna()
        sensors_df4 = sensors_df3.sort_values('TIMESTAMP').drop_duplicates(keep='last')
        sensors_df4 = sensors_df4.tail(30)
        sensors_df5 = sensors_df4.drop(columns=['tmp', 'vpd'])
        motion_df = sensors_df.drop(columns=['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'tmp', 'vpd'])
        valves_df = sensors_df5.loc[sensors_df5 > 60, 'Fee'] = 'Active'
        motion_last_seen = motion_df[motion_df['is_motion'] == 1].iloc[-1]['TIMESTAMP']
#   _______________________________________________________________________________________________________

    while True:
        define_data_frames()
        update_displayed_data(sensors_df4)
        time.sleep(1)
#   _______________________________________________________________________________________________________

try:
    main()
except:
    col1, col2, col3 = st.columns(3)

    with col2:
        st.image('waiting_image_2.jpg', use_column_width=False)
        st.title("Collecting field data........")