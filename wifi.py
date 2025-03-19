
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