p = int(input("enter p : "))
g = int(input("enter g : "))

x1, x2 = int(input("enter x1 : ")), int(input("enter x2 : "))
y1, y2 = pow(g, x1) %  p, pow(g, x2) % p
k1, k2 = pow(y2,x1) %  p, pow(y1, x2) % p

print(k1 == k2)