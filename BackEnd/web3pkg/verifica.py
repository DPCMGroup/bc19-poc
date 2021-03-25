import hashlib

m = hashlib.sha256()

m.update(b"prova prova prova")

x = m.digest()

string = "0x" + "".join([hex(b)[2:] for b in bytearray(x)])
print(string)
