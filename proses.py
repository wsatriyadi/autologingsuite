from lib.eksekusi import gsuite
from lib.penanganancsv import bukacsv
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')
request = config['REQUEST API']
proses = config.getboolean('PROSES','headless')

akun = bukacsv.bukaberkas("accounts.csv")
for index, row in akun.iterrows():
    print("Proses "+row['user']+" request api "+request['jumlah'])

    minta = gsuite.requestjumlah(request,proses,row)
    time.sleep(2)
    proses = gsuite.centangcloud(request,proses,row)