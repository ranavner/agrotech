import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv('fixed.csv')

df = get_data()

placeholder = st.empty()

with placeholder.container():

    st.title("Agrotech Project Dashboard")

    Sensor1, Sensor2, Sensor3, Sensor4 = st.columns(4)

    Sensor1.metric(
        
        label="Sensor 1 RH",
        value=5
    )
    Sensor2.metric(
        
        label="Sensor 2 RH",
        value=45
    )
    Sensor3.metric(
        
        label="Sensor 3 RH",
        value=66
    )
    Sensor4.metric(
        
        label="Sensor 4 RH",
        value=234
    )

Sensor2.line_chart(df)
df = pd.read_csv('fixed.csv')
st.write(df)
time.sleep(1)