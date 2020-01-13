import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname_ex(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + str(IPAddr))