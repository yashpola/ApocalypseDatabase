import hashlib

h = hashlib.new('sha256')
h.update(b'DELETED')
print(h.hexdigest())
