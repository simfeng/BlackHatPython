import socket

target_host = "www.baidu.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create connect client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# accept some data
response = client.recv(4096)

print response
