# Add config file

You can find `example.config.py` file with WiFi name and password. Please create new one `config.py` file with your credentials.

## Flash ESP

MicroPython docs you can find [here](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html)

## Erase

In order to erase your esp please use this `esptool.py --port /dev/ttyUSB0 erase_flash`

## Download firmware

[Here](https://micropython.org/download/ESP8266_GENERIC/) you can find a most recent generic firmware. Please download it. Rename it `firmware.bin` and move it to the folder where you can easily find it

# Flash

In order to flash your ESP run this script in a folder with firmware

`esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 firmware.bin`

You can use [PyMakr](https://docs.pycom.io/gettingstarted/software/vscode/) extension for Vs code or any other tool

Use this scrip to connect via cmd:

`picocom /dev/ttyUSB0 -b9600`

# HTTP Server

ESP started a HTTP server which you can find in `http_server` folder. Please be aware that you should be connected to the same WiFi. After server is started you can go to an IP which you can find in logs

`network config: ('192.168.0.104', '255.255.255.0')`

In `public` folder you will find an html document which is served
