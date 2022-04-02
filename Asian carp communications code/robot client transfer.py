    
def client(ip, port, message):
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
            
            print(input_)
            
            sock.sendall(bytes(str('good'), 'ascii'))    #request input
    
