import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"Hello World", ('localhost', 5000))
print("Sent: Hello World")
