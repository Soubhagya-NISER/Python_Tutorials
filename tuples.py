n = [1,2,3,4,5,6.7]
a = tuple(n)
print(a[3])
#a[3] = 8 ----> invalid for tuples
print(a)
b = list(a)
print(b)
c = a.index(3)
d = a.count(1)
print(c,d)