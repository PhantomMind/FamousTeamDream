a = (1, 2, 3, 4)
b = (5, 6, 7)

print(len(a))
print(6 in a, 2 not in a)

c = a + b
print(c)
print(sum(c))


print(min(c), max(c))

m = c[2]
print(m)

a = [1, 'hello', '222222']
b = a.copy()
print(a)
print(b)

b[2] = 'dftgsdutfuygsf'
print(a)
print(b)

print(c.__sizeof__())





