text = input("Enter a string: ").lower()
text = [ord(i) - 97 for i in text]
print(text)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

def encrypt(text, a, b):
    cipher = [(a * i + b) % 26 for i in text]
    return cipher

def decrypt(cipher, a, b):
    a_inv = mod_inverse(a,26)
    plain = [(a_inv * (i - b)) % 26 for i in cipher]
    return plain

cipher = encrypt(text, a, b)
ct = ''.join([chr(i + 97) for i in cipher])
print(ct)
plain = decrypt(cipher, a, b)
pt = ''.join([chr(i + 97) for i in plain])
print(pt)
