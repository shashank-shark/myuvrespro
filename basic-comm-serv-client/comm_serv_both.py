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
def send (channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)

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
