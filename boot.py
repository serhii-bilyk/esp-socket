import config

def do_connect():
    import network
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWD)

        while not sta_if.isconnected():
            print(config.WIFI_SSID, config.WIFI_PASSWD)
    print('network config:', sta_if.ipconfig('addr4'))
    
do_connect()
 