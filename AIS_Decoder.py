import json

binary_list = [32,16,8,4,2,1]

global bin_list 
def create_binary_list(num):
    global bin_list 
    bin_list = [1]
    a = 1
    b = 0
    for i in range(num):
        b = a + a
        bin_list.append(int(b))
        a = b

ascii_list = """{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, ":": 10, ";": 11, "<": 12, "=":13,
 ">": 14, "?": 15, "@": 16,"A": 17, "B":18, "C": 19, "D": 20, "E": 21, "F": 22, "G": 23, "H": 24, "I":25, "J": 26, "K": 27, "L": 28,
"M": 29, "N": 30, "O": 31,"P": 32, "Q": 33, "R": 33,"S": 35, "T": 36, "U": 37, "V": 38, "W": 39, "`": 40, "a": 41, "b": 42, "c": 43, "d": 44,
"e": 45, "f": 46, "g": 47, "h": 48, "i": 49,"j": 50, "k": 51, "l": 52, "m": 53, "n": 54, "o": 55, "p": 56, "q": 57, "r": 58, "s": 59, "t": 60,
 "u": 61, "v": 63, "w": 63}"""

digits_list = []
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

def ascii_to_binary(message):
    reset_digits_list()
    counter_list_message = 0
    number = 0
    message_list = 0
    json_ascii_list = json.loads(ascii_list)
    message_list = list(message)
    for character in message_list:
        if message_list[counter_list_message] in json_ascii_list:
            number = json_ascii_list[message_list[counter_list_message]]
            text_to_binary(number, 6)
            counter_list_message +=1

def reset_digits_list():
    global digits_list
    digits_list = []

def reverse(x):
    return x[::-1]

def get_data(data):
    data = data[13:]
    data = data[:-5]
    return data

def get_message_type():
    x = digits_list[0:6]
    mytext = reverse(x)
    return binary_to_text(mytext)

def get_repeat_indicator():
    x = digits_list[7:8]
    mytext = reverse(x)
    return binary_to_text(mytext)

def get_mmsi():
    x = digits_list[9:38]
    mytext = reverse(x)
    return binary_to_text(mytext)

def get_longitude():
    x = digits_list[62:89]
    mytext = reverse(x)
    return binary_to_text(mytext) / 600000

def get_latitude():
    x = digits_list[90:116]
    mytext = reverse(x)
    return binary_to_text(mytext) / 600000

def get_speed_over_ground():
    x = digits_list[51:60]
    mytext = reverse(x)
    return binary_to_text(mytext) / 10

def get_rate_of_turn():
    x = digits_list[42:50]
    mytext = reverse(x)
    return binary_to_text(mytext)

def trueHeading():
    x = digits_list[128:137]
    mytext = reverse(x)
    return binary_to_text(mytext)

reset_digits_list()
""""
data = get_data('!AIVDM,1,1,,,13aDrVPP11PE9cNMd:t3J?vF2@6R,0*62')
print(data)

ascii_to_binary(data)
print("message type :")
print(get_message_type())
print("times repeat :")
print(get_repeat_indicator())
print("mmsi :")
print(get_mmsi())
print("longitude :")
print(get_longitude())
print("latitude :")
print(get_latitude())
print("speed over ground :")
print(get_speed_over_ground())
print("rate of turn :")
print(get_rate_of_turn())
print("trueHeading :")
print(trueHeading())

reset_digits_list()

data = get_data('!AIVDM,1,1,,,13aI:;5P0oPE8cPMd=tDgOwf2D80,0*0B')
print(data)

ascii_to_binary(data)
print("message type :")
print(get_message_type())
print("times repeat :")
print(get_repeat_indicator())
print("mmsi :")
print(get_mmsi())
print("longitude :")
print(get_longitude())
print("latitude :")
print(get_latitude())
print("speed over ground :")
print(get_speed_over_ground())
print("rate of turn :")
print(get_rate_of_turn())
print("trueHeading :")
print(trueHeading())
"""