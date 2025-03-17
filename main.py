from machine import Pin

# boot.py -- run on boot-up
import socket

def socket_connect():
    addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
    addr = addr_info[0][-1]
    s = socket.socket()
    s.connect(addr)
    print('connected')
    led = Pin(2, Pin.OUT)
    led.low()

socket_connect()