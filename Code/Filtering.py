import serial
import csv
import time

	
payload = []


def getdata(ser):
    t_end = time.time() + 7
    while time.time() < t_end:
    	payload.append(ser.read())
    
    
    return payload


srl = serial.Serial("COM3", 57600,timeout=5)
payload=getdata(srl)

with open(r'D:\PROJECTCSV\intentionaleyeblink7s.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow(payload)