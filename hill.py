import numpy as np
def encypt(text,key):
    pt_matrix = [text[i:i+2] for i in range(0,len(text),2)]
    res = np.dot(pt_matrix,key).tolist()
    ct = ''.join([chr((i[j] % 26) + 97) for i in res for j in range(len(i))])
    print(ct)
    return res

def decrypt(cipher,key):
    kInverse = np.linalg.inv(key).tolist()
    res = np.dot(cipher,kInverse).tolist()
    pt = ''.join([chr((int(i[j]) % 26) + 97) for i in res for j in range(len(i))])
    print(pt)

text = input("Enter a string: ").lower()
text = [ord(i) - 97 for i in text]
key = [[1,2],[2,3]]
cipher = encypt(text,key)
decrypt(cipher,key)