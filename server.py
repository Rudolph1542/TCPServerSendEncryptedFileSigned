import nacl.utils
import socket

CHUNK_SIZE = 4096

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('127.0.0.1',65432))
soc.listen(1)
x,ad=soc.accept()
print(f'{ad} Conectado')

with open('recived.txt', "wb") as filee:
    chunk = x.recv(CHUNK_SIZE)
    while chunk:
        filee.write(chunk)
        chunk = x.recv(CHUNK_SIZE)
    print('Se recibió archivo')
    soc.close()