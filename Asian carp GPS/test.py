import serial
import datetime
import pynmea2
import csv
from time import time

ser = serial.Serial("COM8", baudrate=38400, timeout = 1)

ser.flushInput()
ser.flushOutput()


while True:

    ser.flushInput()#flush input, the buffer fills up so fast. We want data read to be fresh. 
    ser.readline() #out next message that could be invalid
    ser.readline() #out next message that could be invalid
    ser.readline() #out next message that could be invalid
    
    message1 = ser.read_until('$GNGLL') #abitrary, reads in a good chunk of data
    message1 = message1.decode('cp1252').replace("\n", "-----").replace("\r", "") #decode all the wacky characters serial gives you
    message1 = message1.split('-----') #again arbitrary delimiter to split up the good chunk of data
    
    for message in message1: #combs through the good chunk of data for $GNRMC command that contains all navigation data
        try:                 #this is just a patch to get us up to speed will come up with better way eventually
            #print(message)
            if str(message[0:6]) == '$GNRMC':
                parsed_message = pynmea2.parse(message) #pase the message.
                
                lat = parsed_message.latitude           #lat
                long = parsed_message.longitude         #long
                vel = parsed_message.spd_over_grnd      #velocity
                #print([lat,long,vel])
                
                with open('eggs.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    
                    spamwriter.writerow([time(),lat,long,vel])
                print([lat,long,vel])

                                
        except:
            #print('no balls')
            pass

                
        
        
    #ser.flushInput()
        
        #gga = pynmea2.parse(message)
        
        
##        try:
##            message = message1.decode("utf-8").replace("\n", "-----").replace("\r", "")
##            data = pynmea2.parse(message)
##        except Exception as e:
##            #skip invalid messages
##            print(e) 
##            continue
##
##        
##        #print(ser.in_waiting)
##        header = message.split(',')[0]
##        #print("\n")
##        #print(header)
##        #print(str(header))
##
##        if str(header) == "$GNGLL": #latitiude/longutide handler
##            print('lat/long:' + str([data.latitude, data.longitude]))
##            pass
##
##        if str(header) == "$GNRMC": #velocity handler
##            pass
##            #print(data.fields)
##            print(data.spd_over_grnd)
##            #print("\n")
        
        #value = getattr(parsed_message, field[1])
    ##    for field in data.fields:
    ##        #print(parsed_message.fields)
    ##        
    ##        value = getattr(data, field[1])
    ##        print(f"{field[0]:40} {field[1]:20} {value}")
        
        

        
        #nmea_data += nmea_sentence
        

        #print(gga)
    ser.flushInput() #flush after 20 reads
    buff_index = 0
