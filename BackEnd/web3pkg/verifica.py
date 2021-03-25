import hashlib

m = hashlib.sha256()

m.update(b"prova 1 2 3")

x = m.digest()

string = "0x" + "".join([hex(b)[2:] for b in bytearray(x)])
print(string)
