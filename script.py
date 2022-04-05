import speedtest
from datetime import datetime
import csv 
import os 
import subprocess

def get_path_to_csv():
    #returns the path to the CSV file in which 
    #the values are stored 
    return os.getcwd() + '/internet-speed.csv' 

def location(): 
    #asks the user the location and returns it
    print('Location:')
    return input() 

def date(): 
    #returns the current date in MM/DD/YYYY
    return datetime.now().strftime('%m.%d.%y')

def timestamp():
    #returns the current hours in HH:MM
    return datetime.now().strftime('%H:%M')

def to_Mbs(speed): 
    #convert the speed from bits/s to Mbps and rounds it
    return round(speed * (10**-6))

def download_speed():
    #returns download speed
    return to_Mbs(speedtest.Speedtest().download())

def upload_speed():
    #returns upload speed
    return to_Mbs(speedtest.Speedtest().upload())

def cappuccino_price(): 
    #asks the user the price of a cappucino and returns it
    print('Cappuccino Price:')
    return input() 

def wifi_name():
    #code based on this thread https://gist.github.com/keithweaver/00edf356e8194b89ed8d3b7bbead000c
    #it returns the WiFi network the Mac is connected to  
	process = subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'], stdout=subprocess.PIPE)
	out, err = process.communicate()
	process.wait()

	wifi_info = {}
	for line in out.decode("utf-8").split("\n"):
		if ": " in line:
			key, val = line.split(": ")
			key = key.replace(" ", "")
			val = val.strip()

			wifi_info[key] = val

	return wifi_info["SSID"]


parameters = [date, timestamp, location, wifi_name, download_speed, upload_speed, cappuccino_price]

#opens the csv file in the append mode to add new info 
with open(get_path_to_csv(),  'a') as csv_file:   
    #writes each parameter value to the CSV file 
    csv.writer(csv_file).writerow([f() for f in parameters])