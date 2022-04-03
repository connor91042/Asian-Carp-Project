import socket
from pi_hat_controller import pi_hat
from play_sound import sound_card_
from LOG_GPS_from_usb import log_navigation_data
import _thread
import csv
from time import time


class robot_manual():

    def __init__(self):
        self.hat = pi_hat()
        self.last_button = 0    #to toggle sound
        self.play_sound = False  #state of sound
        self.sound_card = sound_card_()
        self.sound_card.play_sound()
        
        self.usb_log = log_navigation_data()
        self.angle = 0
        self.speed = 0

        #start data logging thread
        #_thread.start_new_thread(self.log_the_damn_data(), 'thread 1')

    def client(self, ip, port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            #this will contain the entire message. 
            sock.connect((ip, port))                 #connect to server at IP
            
            #message is the status the robot can send back to the bot.
            #[bot#, status, lat, long, speed, bearing(degrees pos from north)] rn status = good
            #test status = [bot1, 'good', '10', '-85', 1, 45]
            #print('connected')
            
            
            sock.sendall(bytes(str('manual'), 'ascii'))    #send status message

            
            while True:
                
                input_ = str(sock.recv(1024), 'ascii')
                #print(input)
                angle, speed, x_button = self.parse_server_data(input_)
                self.hat.update_servo(angle)   #adjust servo angle
                self.hat.ramp_thruster(speed)  #adjust servo ramp
                self.toggle_sound(x_button)    #toggle sound output
                sock.sendall(bytes(str('good'), 'ascii'))    #request input

                with open('input_data.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([time(), angle, speed])
                

    def parse_server_data(self,data):
        data = data[1:-1]
        data = data.split(',')
        angle = float(data[0])
        self.angle = angle
        speed = float(data[1])
        self.speed = speed
        x_button = float(data[2])
        
        
        #angle, speed = data.split(',')
        #data = [angle,speed]
        return angle,speed, x_button
        #return data

    def toggle_sound(self,button_value):
        if int(button_value) == 1 and int(self.last_button) == 0: #grab rising edge
            self.play_sound = not(self.play_sound)      #toggle play sound
            self.last_button = button_value

            if self.play_sound:    #decision tree for sound
                self.sound_card.sound_volume(100) #turn on sound
            else:
                self.sound_card.sound_volume(0) #mute
            
        else:
            self.last_button = button_value

    def log_the_damn_data(self):
        self.usb_log.log_GPS_data([self.angle,self.speed]) #log the data
        

bot = robot_manual()
bot.client('192.168.1.3',5001,'')
    


#client('192.168.1.2',5001,'')
