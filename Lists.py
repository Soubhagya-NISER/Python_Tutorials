a = 0
n = [2,3,4,6,7,8]
a = n[0]

for i in  n:
    if a<i:
        a = i
print(a)

m = [[1,2,3],[4,5,6],[7,8,9]]
#m[1][2] = 20
print(m[1][2])

k = []
for i in m:
    for j in i:
        k.append(j)
print(m)
print(k)
print(5 in k)

p = k.copy()
p[0] = 100
print(p)
print(k)
del(p)

o = ['ram','krishna','baba']
o.sort(key = len)
print(o)

k.append(10)
k.insert(0,0)
print(k)

k.extend([0,5,5,2,10,10,10,6,1,8])

for i in k:
    h = k.count(i)
    if h>=2:
        for j in range(0,h-1):
            k.remove(i)
print(k)
print(sorted(k))
