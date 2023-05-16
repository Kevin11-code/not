from math import gcd

def primitiveRoot(m):
    root = []
    required_set = set(i for i in range(1, m) if gcd(i,m) == 1)
    for i in range(1, m):
        actual_set =set(pow(i,p) % m for p in range(1,m))
        if actual_set == required_set:
            root.append(i)
    return root

p = 7
print(primitiveRoot(p))