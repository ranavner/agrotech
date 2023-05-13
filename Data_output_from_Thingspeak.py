import csv
from urllib.request import urlopen
import json
import time
import pandas as pd

# this line is made on the new branch!
# this line is made on the new branch!

# ----------------------------------------------------------
# thingspeak api request setup
READ_API_KEY = '42FNHOI2AE2H4VTG'
CHANNEL_ID = '2076223'
NUMBER_OF_SENSORS = 4
is_header = 0

# ----------------------------------------------------------


def add_sensor_to_list(it):
    new_it = "Sensor " + str(it)
    return new_it


header = [("Sensor " + str(i)) for i in range(1, NUMBER_OF_SENSORS + 1)]


def create_csv_header():
    # create csv header
    with open('fixed.csv', 'a') as t:
        writer = csv.writer(t)
        writer.writerow(header)


def get_data_from_thingspeak():
    time_start = time.perf_counter()
    # executing get command from thingspeak every half a second
    while time.perf_counter() - time_start <= 5:   # while loop runs for 5 seconds
        ts = urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"
                     % (CHANNEL_ID, READ_API_KEY))

        response = ts.read()
        data = json.loads(response)
        print(data)
        # only once - creating the csv's header:
        # if is_header == 0:
        #     create_csv_header(data)
        #     is_header = 1
        tmp_data2 = [data['created_at'], data['field1'], data['field2'], data['field3']]
        print(tmp_data2)
        # print(a + "    " + b + "    " + c + "    " + d)    # python print
        time.sleep(0.5)

        # creating a csv file organizing the data
        with open('fixed.csv', 'a') as t:
            writer = csv.writer(t)
            writer.writerow(tmp_data2)

        ts.close()


def analyse_data():
    db = pd.read_csv('fixed.csv')
    print(db)


if __name__ == "__main__":
    create_csv_header()
    get_data_from_thingspeak()      # creating a csv data for 5 seconds
    # need to get data from image
    analyse_data()

