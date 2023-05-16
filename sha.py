from hashlib import sha1

def sha1_hash(msg):
    return sha1(msg).hexdigest()

msg = b'meet pithadia'
print(sha1_hash(msg))

