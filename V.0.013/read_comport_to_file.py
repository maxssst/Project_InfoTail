import serial
import time
import requests


r = serial.Serial('com3', 9600)
#f = open('sensor_1_temperature.txt', 'x')
f = open('sensor_1_temperature.txt', 'w')
while True:
    income_data = str(r.readline())
    e = time.perf_counter()
    local_time = time.ctime(e)
    # l = round(e, 2)
    print(income_data)
    f = open('sensor_1_temperature.txt', 'a')
    f.write(str(income_data) + str(local_time) + 'sec' + '\n')
    time.sleep(2)
f.close
