import json

# Binary values for ASCII-to-binary conversion
binary_list = [32, 16, 8, 4, 2, 1]

# Global variable to store binary values
global bin_list

# Function to create a list of binary values up to a given number of digits
def create_binary_list(num):
    global bin_list 
    bin_list = [1]
    a = 1
    b = 0
    for i in range(num):
        b = a + a
        bin_list.append(int(b))
        a = b

# Dictionary to map ASCII characters to binary values
ascii_list = """{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ":": 10, ";": 11, "<": 12, "=":13,
 ">": 14, "?": 15, "@": 16,"A": 17, "B":18, "C": 19, "D": 20, "E": 21, "F": 22, "G": 23, "H": 24, "I":25, "J": 26, "K": 27, "L": 28,
"M": 29, "N": 30, "O": 31,"P": 32, "Q": 33, "R": 33,"S": 35, "T": 36, "U": 37, "V": 38, "W": 39, "`": 40, "a": 41, "b": 42, "c": 43, "d": 44,
"e": 45, "f": 46, "g": 47, "h": 48, "i": 49,"j": 50, "k": 51, "l": 52, "m": 53, "n": 54, "o": 55, "p": 56, "q": 57, "r": 58, "s": 59, "t": 60,
 "u": 61, "v": 63, "w": 63}"""

# Global variable to store binary digits
digits_list = []

# Function to convert a number to binary, given the number of digits
def text_to_binary(number, rounds):
    counter = 0
    value_item = 0
    global digits_list
    
    for i in range(rounds):
        if number >=binary_list[counter]:
            value_item = binary_list[counter]
            
            number -= value_item
            digits_list.append("1")
            counter +=1
        elif number <binary_list[counter]:
            
            digits_list.append("0")
            counter +=1

# Function to convert a binary number to its decimal value
def binary_to_text(text):
    text_list = 0
    text_list = list(text)
    counter = 0
    value_item = 0
    global bin_list
    
    create_binary_list(len(text_list))
    for charachters in text_list:
        if text_list[counter] == '1':
            value_item += bin_list[counter]
            counter +=1
        elif text_list[counter] == '0':
            counter +=1
    return value_item

# ascii_to_binary converts an ASCII string to a binary string
def ascii_to_binary(message):
    # reset the digits_list global variable to an empty list
    reset_digits_list()
    
    # counter to keep track of the current character in the message
    counter_list_message = 0
    
    # variable to store the binary representation of the current character
    number = 0
    
    # variable to store the message as a list of characters
    message_list = 0
    
    # load the ascii_list JSON object
    json_ascii_list = json.loads(ascii_list)
    
    # convert the message to a list of characters
    message_list = list(message)
    
    # iterate through each character in the message
    for character in message_list:
        # check if the character is in the ascii_list JSON object
        if message_list[counter_list_message] in json_ascii_list:
            # store the binary representation of the character in the number variable
            number = json_ascii_list[message_list[counter_list_message]]
            # convert the number to binary and add it to the digits_list global variable
            text_to_binary(number, 6)
            # increment the counter
            counter_list_message +=1

# reset_digits_list sets the digits_list global variable to an empty list
def reset_digits_list():
    global digits_list
    digits_list = []

# reverse reverses the order of the characters in a string
def reverse(x):
    return x[::-1]

# get_data extracts the data from a string
def get_data(data):
    # remove the first 14 characters from the data string
    data = data[14:]
    # remove the last 7 characters from the data string
    data = data[:-7]
    return data

# get_message_type returns the message type from the digits_list global variable
def get_message_type():
    # get the first 6 characters from the digits_list global variable
    x = digits_list[0:6]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text
    return binary_to_text(mytext)

# get_repeat_indicator returns the repeat indicator from the digits_list global variable
def get_repeat_indicator():
    # get the 8th character from the digits_list global variable
    x = digits_list[7:8]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text
    return binary_to_text(mytext)

# get_mmsi returns the MMSI from the digits_list global variable
def get_mmsi():
    # get the characters from the 9th to the 38th position in the digits_list global variable
    x = digits_list[9:38]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text
    return binary_to_text(mytext)

# get_longitude returns the longitude from the digits_list global variable
def get_longitude():
    # get the characters from the 62nd to the 89th position in the digits_list global variable
    x = digits_list[62:89]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text and divide by 600000 to get the longitude value
    return binary_to_text(mytext) / 600000

# get_latitude returns the latitude from the digits_list global variable
def get_latitude():
    # get the characters from the 90th to the 116th position in the digits_list global variable
    x = digits_list[90:116]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text and divide by 600000 to get the latitude value
    return binary_to_text(mytext) / 600000

# get_speed_over_ground returns the speed over ground from the digits_list global variable
def get_speed_over_ground():
    # get the characters from the 51st to the 60th position in the digits_list global variable
    x = digits_list[51:60]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text, divide by 10, and multiply by 1.852000 to get the speed over ground value
    return round(binary_to_text(mytext) / 10 * 1.852000, 2)

# get_rate_of_turn returns the rate of turn from the digits_list global variable
def get_rate_of_turn():
    # get the characters from the 42nd to the 50th position in the digits_list global variable
    x = digits_list[42:50]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text
    return binary_to_text(mytext)

# trueHeading returns the true heading from the digits_list global variable
def trueHeading():
    # get the characters from the 128th to the 137th position in the digits_list global variable
    x = digits_list[128:137]
    # reverse the order of the characters
    mytext = reverse(x)
    # convert the binary string to text
    return binary_to_text(mytext)

# reset the digits_list global variable to an empty list
reset_digits_list()


