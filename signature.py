from ecdsa import SigningKey
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from hashlib import sha256
def rsakeys():  
    length=1024
    privatekey = RSA.generate(length, Random.new().read)  
    publickey = privatekey.publickey()  
    return privatekey, publickey


def encrypt(rsa_publickey,plain_text):
    cipher = PKCS1_OAEP.new(rsa_publickey)
    cipher_text=cipher.encrypt(plain_text)
    print("encrypted message : ",cipher_text)
    return cipher_text

def decrypt(rsa_privatekey,b64cipher):
    cipher = PKCS1_OAEP.new(rsa_privatekey)
    plaintext = cipher.decrypt(b64cipher)
    print("decrypted message : ",plaintext)
    return plaintext

msg = b'siddhi muni'
print("Initial message : ",msg)
privAlice,pubAlice = rsakeys()
print("A's Public key : ",pubAlice)
print("A's Private key : ",privAlice)
privBob,pubBob = rsakeys()
print("B's Public key : ",pubBob)
print("B's Private key : ",privBob)

encryptedMsg = encrypt(pubBob,msg)
hash = sha256(msg).hexdigest()
res = bytes(hash, 'utf-8')
private_key = SigningKey.generate()
vk = private_key.verifying_key
signature = private_key.sign(res)
print("signature: ",signature)

#decryption
decryptedMsg = decrypt(privBob,encryptedMsg)
hash = sha256(decryptedMsg).hexdigest()
res = bytes(hash, 'utf-8')
print(vk.verify(signature,res))