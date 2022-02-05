import socket
import sys

from time import sleep
import random

import signal

import skywriter

some_value = 5000

def skywrite():
    
    #Create a UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host, port = '192.168.0.2', 65000
    server_address = (host, port)
    
    
    message = ('hello from the pi'.encode())
    sock.sendto(message, server_address)

    @skywriter.flick()
    def flick(start,finish):
        print('Got a flick!', start, finish)
        message = (('F' + ' ' + start + ' ' + finish).encode())
        sock.sendto(message, server_address)

    @skywriter.airwheel()
    def spinny(delta):
        global some_value
        some_value += delta
        if some_value < 0:
            some_value = 0
        if some_value > 10000:
            some_value = 10000
        print('Airwheel:', some_value/100)
        message = ('A'.encode())
        sock.sendto(message, server_address)

    @skywriter.double_tap()
    def doubletap(position):
        print('Double tap!', position)
        message = (('DTA' + ' ' + position).encode())
        sock.sendto(message, server_address)

    @skywriter.tap()
    def tap(position):
        print('Tap!', position)
        message = (('TA' + ' ' + position).encode())
        sock.sendto(message, server_address)

    @skywriter.touch()
    def touch(position):
        print('Touch!', position)
        print(type(position))
        message = (('TO' + ' ' + position).encode())
        sock.sendto(message, server_address)
        

    signal.pause()

skywrite()