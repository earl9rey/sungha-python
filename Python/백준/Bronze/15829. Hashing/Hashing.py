l = int(input())
s = input()
m = 1234567891

hash = 0
for i in range(l) :
    hash += (ord(s[i]) - 96) * (31 ** i)

print(hash % m)