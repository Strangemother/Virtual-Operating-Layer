import socket

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to all interfaces on port 5000
sock.bind(('0.0.0.0', 5000))

print("Listening for UDP messages on port 5000...")

# Receive message
data, addr = sock.recvfrom(1024)  # buffer size 1024 bytes
print(f"Received: {data.decode()} from {addr}")
