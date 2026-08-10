import socket

target_host = input("Enter target IP or domain: ")  
target_port = 80

# Set up TCP IPv4 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2) # Timeout so script doesn't hang

result = s.connect_ex((target_host, target_port))

if result == 0:
    print("Port" ,target_port , "is OPEN on" ,target_host,"!")
else:
    print("Port" ,target_port,"is CLOSED or filtered.")

s.close()
