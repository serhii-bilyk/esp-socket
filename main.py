import socket
import network

def client_program():
    host = '192.168.0.102'  # as both code is running on same pc
    port = 3002  # socket server port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

# client_program()

def wifi():
    
    # Create an access point (AP) instance
    ap = network.WLAN(network.AP_IF)

    # Activate the access point
    ap.active(True)

    # Set the SSID and password
    ssid = 'ESP8266-AP'
    password = '123456789'

    # Configure the access point
    ap.config(essid=ssid, password=password)

    # Print the IP address of the access point
    print('Access Point started with IP:', ap.ifconfig()[0])
    
wifi()