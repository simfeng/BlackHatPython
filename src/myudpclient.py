import socket

target_host = "www.baidu.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
print ">>> sent data"
client.sendto("AAABBBBCCC", (target_host, target_port))

# receive data 
print ">>> receive data"
data, addr = client.recvfrom(4096)

print data
