import pandas as pd
import numpy as np
import csv
import time
import os

header = ['sensor1', 'sensor2']
data = [1, 2]

os.remove('fixed2.csv')

with open('fixed2.csv', 'a') as t:
    writer = csv.writer(t)
    writer.writerow(header)
    for seconds in range(200):
        writer.writerow(data)
        t.flush()

        time.sleep(1)