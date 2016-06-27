import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("Criando um port scaner em python")
remotehost = 'www.pythonforbeginners.com'
ip = socket.gethostbyname(remotehost)
port = 80

print("Dados remotehost: "+ remotehost)
print("Dados ip: "+ ip)

if s.connect_ex((ip, port)):
    print("Porta" + port + "esta fechada")
else:
    print("Porta" + str(port) + "esta Aberta")


      