text = input("Enter text : ").lower()
key = int(input("enter key : "))
cipher = ''
for i in text:
    if i.isnumeric():
        cipher += str((int(i) + key) % 10)
    else:
        cipher += chr((ord(i) + key - 97) % 26 + 97)
print(cipher)
decipher = ''
for i in cipher:
    if i.isnumeric():
        decipher += str((int(i) - key) % 10)
    else:
        decipher += chr((ord(i) - key - 97) % 26 + 97)
print(decipher)
