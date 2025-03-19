import socket

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 3002)[0][-1]  # Listen on all available interfaces on port 80
    s = socket.socket()  # Create a socket
    s.bind(addr)  # Bind the socket to the address and port
    s.listen(1)  # Listen for incoming connections
    
    print('Listening on', addr)
    
    while True:
        cl, addr = s.accept()  # Accept a new client connection
        print('Client connected from', addr)
        
        while True:
            data = cl.recv(1024)  # Receive data from the client
            if not data:
                break  # Break if no data is received (client disconnected)
            print("Received:", data)
            cl.send(data)  # Send the same data back to the client (echo server)
        
        cl.close()  # Close the client connection
        print('Client disconnected')

start_server()