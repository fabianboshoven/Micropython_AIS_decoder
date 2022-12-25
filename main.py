import socket
import AIS_Decoder

import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20
i2c = machine.I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Set up constants for the server
LOCAL_IP = "192.168.1.215"
LOCAL_PORT = 10110
BUFFER_SIZE = 1024

# Set up the LCD


# Clear the display
lcd.clear()
lcd.putstr("AIS decoder v0.9" + "\n")
lcd.putstr("made by fabian" + "\n")
lcd.putstr("UDP server up" + "\n")
lcd.putstr("listening for ais " + "\n")


# Create the UDP socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Bind the socket to the local IP and port
UDPServerSocket.bind((LOCAL_IP, LOCAL_PORT))



# Listen for incoming datagrams
number = 0
mmsi =  ""
while True:
    try:
        # Reset the digits_list
        digits_list = []
        
        # Receive data from the client
        bytes_address_pair = UDPServerSocket.recvfrom(BUFFER_SIZE)
        message = bytes_address_pair[0]
        data = AIS_Decoder.get_data(message.decode("utf-8"))
        print(data)
        
        # Convert the data to binary and extract information
        AIS_Decoder.ascii_to_binary(data)
        print("message type :")
        print(AIS_Decoder.get_message_type())
        print("times repeat :")
        print(AIS_Decoder.get_repeat_indicator())
        print("mmsi :")
        print(AIS_Decoder.get_mmsi())
        if AIS_Decoder.get_mmsi() != mmsi:
            lcd.clear()
            lcd.putstr("mmsi : " + str(AIS_Decoder.get_mmsi()) + "\n")
            lcd.putstr("speed : " + str(AIS_Decoder.get_speed_over_ground()) + "\n")
            lcd.putstr("heading : "+ str(AIS_Decoder.trueHeading()) + "\n")
            lcd.putstr("rot : "+ str(AIS_Decoder.get_rate_of_turn()) + "\n")
            
            mmsi = AIS_Decoder.get_mmsi()
        print("longitude :")
        print(AIS_Decoder.get_longitude())
        print("latitude :")
        print(AIS_Decoder.get_latitude())
        print("speed over ground :")
        print(AIS_Decoder.get_speed_over_ground())
        print("rate of turn :")
        print(AIS_Decoder.get_rate_of_turn())
        print("trueHeading :")
        print(AIS_Decoder.trueHeading())
        print("number :")
        print(number)
        number += 1
        
    except Exception as e:
        # Print the exception message and close the socket
        print(e)
        UDPServerSocket.close()

