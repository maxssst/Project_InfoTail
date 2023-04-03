import ftplib
import requests
import datetime
import time
import serial

# -----------------------------READING AND WRITE DATA-----------------------
r = serial.Serial('com3', 9600)

while True:
    today = datetime.datetime.today()
    local_time = today.strftime("%Y_%m_%d_%H.%M.%S")
    fileName = "VESSELname" + local_time + ".txt"
    f = open(fileName, 'w')

    for _ in range(100):
        today1 = datetime.datetime.today()
        local_time1 = today1.strftime("%Y_%m_%d_%H.%M.%S")

        income_data = str(r.readline())
        f = open(fileName, 'a')
        f.write(str(income_data) + str(local_time1) + 'sec' + '\n')
        print(income_data)
        print(fileName)
        f.close

        time.sleep(4)
 # -----------------------------SEND DATA-----------------------
#     USER = 'infoteil'
#     PASS = '!NfoTeIL&%#'
#     HOST = 'infiteil.westeurope.cloudapp.azure.com'
#     PORT = 21
#     # USER = 'max'
#     # PASS = 'max'
#     # HOST = '172.16.45.143'
#     # PORT = 21
    

#     ftp = ftplib.FTP(HOST, USER, PASS)
#     ftp.login(USER, PASS)

#     # Конструкция открывает файл в заданном режиме и в любом случае закроет его
#     with open(fileName, 'rb') as upload_file:
#         ftp.storbinary('STOR ' + fileName, upload_file)
#         print("file: " + fileName +  " sent to the " + HOST)
#     # Закрываем FTP соединение
#     ftp.close
#  # -----------------------------SEND DATA-----------------------
