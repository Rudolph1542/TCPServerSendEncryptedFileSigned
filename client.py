import nacl.secret as pynaclSecret
import nacl.utils as pynacl
from Crypto.Cipher import ChaCha20
from nacl.signing import SigningKey
import socket



CHUNK_SIZE = 4096

key = b"9" * 32
c=ChaCha20.new(key=key)
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('127.0.0.1',65432))
print('Conectado')

print('Enviando archivo encriptado')
with open('tosend.txt','rb') as filee:
    data=filee.read(CHUNK_SIZE)
    encData=c.encrypt(data)
    send = SigningKey.generate().sign(encData)
    soc.sendall(send)
    print('Se envió archivo encriptado y firmado')
    soc.close()