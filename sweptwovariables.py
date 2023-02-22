# method 1: using third variable
x = 3
y = 4

z = x
x = y
y = z
print(x)
print(y)

#method 2: without using third variable
a = 2
b = 5
a = a+b
b = a-b
a = a-b
print(a)
print(b)

# method 3:
d = 6
g = 9
d = d^g
g = g^d
d = d^g
print(d)
print(g)

#method 4:
f = 7
k = 10
f,k = k,f
print(f)
print(k)