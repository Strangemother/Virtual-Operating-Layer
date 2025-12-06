import net

var sock = newSocket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
sock.sendTo("localhost", Port(5000), "Hello World")
echo "Sent: Hello World"
