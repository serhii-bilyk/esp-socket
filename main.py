from machine import Pin

# boot.py -- run on boot-up
import socket

# https://docs.micropython.org/en/latest/library/socket.html

def socket_connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket created')
    s.connect(('192.168.0.102', 3001))
    # s.connect(('172.17.0.1', 3001))

    print('connected')
    s.send('hi')
 
    # led = Pin(2, Pin.OUT)
    # led.low()

socket_connect()