import csv
import time
import os
from datetime import datetime
import random

header = ['TIMESTAMP', 'sensor1', 'sensor2', 'sensor3','sensor4', 'sensor5', 'sensor6']

os.remove('fixed2.csv')

with open('fixed2.csv', 'a') as t:
    writer = csv.writer(t)
    writer.writerow(header)
    for seconds in range(10000):
        data = [datetime.now(), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
        writer.writerow(data)
        t.flush()

        time.sleep(1)