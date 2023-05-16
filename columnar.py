# text = input('Enter the text : ')
# key = input('Enter the key :').lower()
text = 'meetab'
key = 'hack' # 2 0 1 3
key = [ord(i) for i in key]
sk = sorted(key)
print("key : ",key)
print("sorted key : ",sk)
priority = []
for i in key:
    priority.append(sk.index(i))
print(priority)
priority2 = [i for i in priority]
if len(text) % len(key) != 0:
    text += '#' * (len(key) - (len(text) % len(key)))
res = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
for i in res:
    print(i)
cipher = ''
for _ in range((len(key))):
    i = priority.index(min(priority))
    for j in range(len(res)):
        cipher += res[j][i]
    priority[i] = 10000
print("Cipher : ",cipher)
# deciphering starts
i=0
c=2
j=0
d=[[0 for _ in range(len(res[0]))] for _ in range(0,len(res))]
while i!=len(cipher):
     text=cipher[i:c]
     c+=2
     i+=2
     pos=priority2.index(j)
     print(pos)
     d[0][pos]=text[0]
     d[1][pos]=text[1]
     j+=1
print(d)
