import socket
import threading
import socketserver
import queue
from threading import Thread


FIFO = queue.Queue()

#setting up the FIFOs for the first 3 robots
bot1_incoming = queue.Queue()
bot2_incoming = queue.Queue()
bot3_incoming = queue.Queue()

bot1_outgoing = queue.Queue()
bot2_outgoing = queue.Queue()
bot3_outgoing = queue.Queue()


RX_FIFO = {"bot1": bot1_incoming,
           "bot2": bot2_incoming,
           "bot3": bot3_incoming}


TX_FIFO = {"bot1": bot1_incoming,
           "bot2": bot2_incoming,
           "bot3": bot3_incoming}




#simulated robot client   (save for later)
class robot_simulated(Thread):
    def __init__(self,):
        pass


    def run(self):
        pass
    




class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self): #Handles the message
        bot_ID = RX_FIFO[(str(self.request.recv(1024), 'ascii'))])


        #bot send time, GPS data, status
        #status = on route to waypoint (specify )
        cur_thread = threading.current_thread()

        
        
        
        response = bytes("data recieved", 'ascii')
        self.request.sendall(response)

        



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass

    
##    def setup_attributes(self):
##        #this section sets up the server's attributes
##        self.pos1 = 0;
##        self.pos2 = 0;
##        self.pos3 = 0;
##        
##        
##        pass
    

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    


    
    
    with server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)
        
        client(ip, port, "bot1")
        client(ip, port, "bot2")
        client(ip, port, "bot3")


        print("oh my there batman")
        server.shutdown()
