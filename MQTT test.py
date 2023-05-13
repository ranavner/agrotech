import paho.mqtt.client as mqtt
import csv
import seaborn as sb
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import re


# MQTT broker details
broker_address = "broker.hivemq.com"
broker_port = 1883


# Callback function when a connection is established with the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code: " + str(rc))
    # Subscribe to the topic upon successful connection
    client.subscribe("agrotech/2023/ran_ran")


# Callback function when a message is received
def on_message(client, userdata, msg):
    print("Random Number: " + str(msg.payload.decode()))

    with open('/Users/ranavner/Desktop/10_5.csv', 'a') as f:
        writer = csv.writer(f)
        string_to_float = float(msg.payload.decode())
        writer.writerow(msg.payload.decode())


# Create a MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

time2 = time.perf_counter()
print(time2)

client.loop_forever()



# מצלמה של esp32
#