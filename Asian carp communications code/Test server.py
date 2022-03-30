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

        message_from_client = str(self.request.recv(1024), 'ascii')
        #print(message_from_client)
        #bot_ID = RX_FIFO[str(message_from_client), 'ascii']


        #bot send time, GPS data, status
        #status = on route to waypoint (specify )
        cur_thread = threading.current_thread()

        
        
        #print('connected to:' + str(bot_ID))
        response = bytes(("hello " + message_from_client), 'ascii')
        self.request.sendall(response)

        



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass    


if __name__ == "__main__":
    
    # Port 0 means to select an arbitrary unused port
    hostname = socket.gethostname() #get host name
    HOST, PORT = socket.gethostbyname(hostname), 5001 #get host ip and choose arbitrary port

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    print(HOST)
    

    
    
    with server:

        
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)

        #main loop
        i = 0
        while True:
            try:
                print('waiting') #gotta do something

            except Exception as e:
                print (e)
                
                server.shutdown() #safely handle the server's shutdown
                break

        
        
