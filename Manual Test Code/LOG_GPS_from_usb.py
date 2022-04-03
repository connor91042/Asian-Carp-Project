import serial
import datetime
import pynmea2
import csv
from time import time


class log_navigation_data():

    def __init__(self):
        

        self.ser = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout = 1) #create serial connection object
        

    def log_GPS_data(self,extra_list):
        #print('I am totally gonna log that fuckin data bro. From one robot to a human')
        last = time()    
        navigation_data = self.get_GPS_coordinates()
        
        with open('navigation_data_log.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            spamwriter.writerow([time()] + navigation_data + extra_list) 
        
           
    def get_GPS_coordinates(self):
        #this module handles getting GPS data from serial. 
        #it returns the large chunk of gps coordinates
        self.ser.flushInput() #flush the input buffer (it fills up fast and is then unusable)
        self.ser.readline() #out next message that could be invalid
        self.ser.readline() #out next message that could be invalid

        message1 = self.ser.read_until('$GNGLL') #abitrary, reads in a good chunk of data
        message1 = message1.decode('cp1252').replace("\n", "-----").replace("\r", "") #decode all the wacky characters serial gives you
        message1 = message1.split('-----') #again arbitrary delimiter to split up the good chunk of data
        for message in message1: #combs through the good chunk of data for $GNRMC command that contains all navigation data

            try:                 #this is just a patch to get us up to speed will come up with better way eventually
                
                if str(message[0:6]) == '$GNRMC':           #this command gives us all navigation data needed

                    parsed_message = pynmea2.parse(message) #pase the message.
                    lat = parsed_message.latitude           #lat
                    long = parsed_message.longitude         #long
                    vel = parsed_message.spd_over_grnd      #velocity
                    return([lat,long,vel])
            except:
                print('no balls')
                pass
            
            

if __name__ == '__main__':
    navigation_log = log_navigation_data()
    #last = time()
    while True:
        navigation_log.log_GPS_data([])
    #print(time()- last)
