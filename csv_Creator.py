import pandas as pd
import numpy as np
import csv
import time
import os
import random

header = ['sensor1', 'sensor2', 'sensor3','sensor4', 'sensor5', 'sensor6']

os.remove('fixed2.csv')

with open('fixed2.csv', 'a') as t:
    writer = csv.writer(t)
    writer.writerow(header)
    for seconds in range(200):
        data = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
        writer.writerow(data)
        t.flush()

        time.sleep(1)