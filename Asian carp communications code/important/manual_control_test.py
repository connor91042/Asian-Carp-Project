import socket
from pi_hat_controller import pi_hat




class robot_manual():

    def __init__(self):
        self.hat = pi_hat()
        

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
                
                angle, speed = self.parse_server_data(input_)
                self.hat.update_servo(angle)
                self.hat.ramp_thruster(speed)
                
                sock.sendall(bytes(str('good'), 'ascii'))    #request input

    def parse_server_data(self,data):
        data = data[1:-1]
        data = data.split(',')
        angle = float(data[0])
        speed = float(data[1])
        #angle, speed = data.split(',')
        #data = [angle,speed]
        return angle,speed
        #return data

bot = robot_manual()
bot.client('192.168.135.86',5001,'')
    


#client('192.168.1.2',5001,'')
