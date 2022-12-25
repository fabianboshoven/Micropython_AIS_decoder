# Micropython_AIS_decoder
A simple AIS decoder for micropython

This code is a Python script that provides functions for encoding and decoding Automatic Identification System (AIS) data. AIS is a maritime communications system that transmits information such as vessel location, speed, and heading to other vessels and shore-based stations.

The main functions of this code are:

    ascii_to_binary(message): This function converts an ASCII string to a binary string. It takes a string message as input and returns a list of binary digits as output.
    reset_digits_list(): This function resets the digits_list global variable to an empty list.
    binary_to_text(text): This function converts a binary string to its decimal value. It takes a string text as input and returns an integer as output.

Other functions in the code include:

    create_binary_list(num): This function creates a list of binary values up to a given number of digits.
    text_to_binary(number, rounds): This function converts a number to binary, given the number of digits.
    reverse(x): This function reverses the order of the elements in a list.
    get_data(data): This function extracts the data from a string.
    get_message_type(), get_repeat_indicator(), get_mmsi(), get_longitude(), get_latitude(), get_speed_over_ground(), get_rate_of_turn(), and trueHeading(): These functions extract specific pieces of information from the digits_list global variable.

Overall, this code is used to decode AIS data. It can be used to receive information about vessel location, speed, and heading in a maritime environment.


Note for displaying the data on the lcd i used this i2c lcd code :
https://peppe8o.com/download/micropython/LCD/lcd_api.py
https://peppe8o.com/download/micropython/LCD/i2c_lcd.py
