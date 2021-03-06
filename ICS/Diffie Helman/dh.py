import random
import socket

server = socket.socket()
PORT = 1234
server.bind(('',PORT))
server.listen(5)
print('Server Started....')
conn,addr = server.accept()
conn.send('Welcome to Diffi-Hellman Server'.encode())
print('Connected to :',addr)
p = conn.recv(1024).decode()
g = conn.recv(1024).decode()
public_client = conn.recv(1024).decode()

p,g,public_client = int(p),int(g),int(public_client)

print('Modulus : ',p,' received from client')
print('Base : ',g,' received from client')

private = random.randint(1,g)
print('Private : ',private)
public_server = (g**private)%p
print('Public Server Key : ',public_server,' sent to client')

key = (public_client**private)%p

conn.send(str(public_server).encode())
print('Public Client Key : ',public_client,' received from client')
print('Key : ',key)
conn.close()
