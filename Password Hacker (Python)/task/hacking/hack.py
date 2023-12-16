import socket
import sys
import string
import itertools
import os
from copy import copy

"""
def brute_force():
    i = 0
    for data in possibilities:
        data_send = "".join(data).encode()
        # print(data_send)
        client_socket.send(data_send)
        response = client_socket.recv(1024).decode()
        if response == "Connection success!":
            print(data)
            return
        #print(data_send)
    password = possibilities
    comb = list()
    while i <= 1:
        i += 1
        #for data in itertools.combinations(possibilities, i):
        for data in itertools.product(password,possibilities):
            data = "".join(data[0])+data[1]
            #print(data)
            comb.append(data)
            data_send = "".join(data).encode()
            #print(data_send)
            client_socket.send(data_send)
            response = client_socket.recv(1024).decode()
            if response == "Connection success!":
                print(data)
                return
            #print(data_send)
        password = copy(comb)
        #print(f"comb = {comb}")
        comb.clear()
        #print(f"password = {password}")
"""
# Calculating binary sum by using bin() and int()
def binary_sum(a, b):
    return int(a, 2) + int(b, 2)
#e.g. a132qw
def upper_and_lower(word):
    # Calculating binary sum by using bin() and int()
    #binary_sum = lambda a, b: bin(int(a, 2) + int(b, 2))
    #created = set()
    #only_letter = ""
    #for l in word:
    #    if l.isalpha():
    #        only_letter += l
    #    else
    #the n combination shoulb be equal the binary count of letters, e.g qwerty => 111111 =>  63+1 combinacoes
    #possibility = [0 for x in range(len(only_letter))]
    #possibility = bytes(len(only_letter))
    #total_possibility = int(bytes([1 for x in range(len(only_letter))]))
    #while int(possibility) <= total_possibility:
    #b.
    possibility = "".join(['0' for x in range(len(word))])
    total_possibility = "".join(['1' for x in range(len(word))])
    while int(possibility, 2) <= int(total_possibility,2):
        #print(f"possibility = {possibility} {type(possibility)} len = {len(possibility)}, word = {word} {type(word)} len = {len(word)}")
        one_try = "".join([l if possibility[i] == '0' or l.isdigit() else l.upper() for i, l in enumerate(word)])
        possibility = str(bin(int(possibility, 2)+1))[2:]
        possibility = "".join(['0' for x in range(len(word)-len(possibility))]) + possibility
        data_send = one_try.encode()
        #print(data_send)
        client_socket.send(data_send)
        response = client_socket.recv(1024).decode()
        if response == "Connection success!":
            print(one_try)
            return True
    return False

# creating the socket
client_socket = socket.socket()
hostname = sys.argv[1]
port = int(sys.argv[2])
address = (hostname, port)

# connecting to the server
client_socket.connect(address)
#possibilities = string.ascii_lowercase + string.digits
#password = ""
#brute_force()
#openning a file

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "passwords.txt"),"r")

for word in file.readlines():
    if upper_and_lower(word.strip()):
        break

# data = sys.argv[3]
# converting to bytes
# data = data.encode()

# sending through socket
# client_socket.send(data)

# receiving the response
# response = client_socket.recv(1024)

# decoding from bytes to string
# response = response.decode()
# print(response)

client_socket.close()
