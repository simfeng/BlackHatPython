import socket
import threading

bind_ip = "0.0.0.0"

bind_port  = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# this is client process thread
def handle_client(client_socket):

    # print client send msg
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    # return a data package
    client_socket.send("ACK!")

    client_socket.close()

while True:

    print ">>> while in ..."
    client, addr = server.accept()
    print '>>> client, addr', client, addr

    print "[*] Accepted connection from : %s:%d" % (addr[0], addr[1])

    # hangup client thread, handle received data
    client_handle = threading.Thread(target=handle_client, args=(client,))
    client_handle.start()
    
        
