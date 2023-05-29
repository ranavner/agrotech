import csv
from urllib.request import urlopen
import json
import time
import pandas as pd
from tkinter import *
import streamlit as st
from streamlit.web import cli as stcli
from os.path import exists
import subprocess
from datetime import datetime

# ----------------------------------------------------------
# thingspeak api request setup
READ_API_KEY = 'UMOB8GG4SVBVXTHA'
CHANNEL_ID = '2076230'
# ----------------------------------------------------------

sensors_csv = 'sensors_csv_' + str(datetime.now()) + '.csv'     # creating a csv with the current timestamp as filename
sensors_header = ['TIMESTAMP', 'Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'is_motion']


def create_csv_header(file_name, header):
    # create csv header
    with open(file_name, 'w') as t:
        writer = csv.writer(t)
        writer.writerow(header)

def get_data_from_thingspeak():
    subprocess.Popen(["streamlit","run","GUI_test.py"])     # running the streamlit server by terminal
    while True:

        ts = urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"
                     % (CHANNEL_ID, READ_API_KEY))

        response = ts.read()
        data = json.loads(response)
        print(data)
        sensors_data = [data['created_at'], data['field1'], data['field2'], data['field3'], data['field4'], data['field5']]
        print(sensors_data)
        with open(sensors_csv, 'a') as s:
            writer = csv.writer(s)
            writer.writerow(sensors_data)
            s.flush()

        
        time.sleep(0.7)
        ts.close()

def main():
    create_csv_header(sensors_csv, sensors_header) # run once for the header
    get_data_from_thingspeak() # loops forever

if __name__ == "__main__":
        main()