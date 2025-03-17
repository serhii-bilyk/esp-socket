# Flash ESP

https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

# Erase

esptool.py --port /dev/ttyUSB0 erase_flash

# Flash

esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 firmware.bin

picocom /dev/ttyUSB0 -b115200
