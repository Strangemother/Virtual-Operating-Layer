import net

var sock = newSocket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
sock.bindAddr(Port(5000))

echo "Listening for UDP messages on port 5000..."

var data: string
var address: string
var port: Port
sock.recvFrom(data, 1024, address, port)
echo "Received: ", data, " from ", address, ":", port
