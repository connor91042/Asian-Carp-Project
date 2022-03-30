import socket
import threading
import socketserver
import queue
from threading import Thread


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))                 #connect to server at IP
        sock.sendall(bytes(message, 'ascii'))    #send message
        response = str(sock.recv(1024), 'ascii') #read back response
        print("Response: {}".format(response))   #print recieved data
        

if __name__ == "__main__":
    
    
    


    ip, port = '192.168.1.3' ,5001 #the server's IP address and port to attach to
    
    client(ip, port, "bot1") #bot 1  
    


        
