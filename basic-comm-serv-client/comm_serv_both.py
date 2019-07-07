# import the necessary libraries first
import select
import socket
import sys
import signal
import _pickle as cPickle
import struct
import argparse

SERVER_HOST = 'localhost'
COMMUNICATION_SERVER_NAME = 'server'

# we will define some of the common utilities for the processess
#---------------------------------------------------------------
def send (channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)

#----------------------------------------------------------------

def recieve (channel):
    size = struct.calcsize ("L")
    size = channel.recv(size)

    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ''
    
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))

    return cPickle.loads(buf)[0]

#-----------------------------------------------------------------

# communication server class here
class CommServer (object):
    """ This communication server is built on select """
    def __init__ (self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []   # to list output sockets

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # enable reusing the socket address
        self.server.setsocketop(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind ((SERVER_HOST, port))
        print ('Server Listening to port : ', port)
        self.server.listen(backlog)

        # for catching the keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

        def sighandler (self, signum, frame):
            """ Clean up the client outputs """
            # close the server
            print ('Shutting down the server')

            # close existing client sockets
            for output in self.outputs:
                output.close()
            
            self.server.close()
        
        def get_client_name (self, client):
            """ Return the name of the client """
            info = self.clientmap[client]
            host, name = info[0][0], info[1]
            return '@'.join((name, host))

