import random
x = 3 + 5j
y = 1 + 2j

print(x.real)
print(x.imag)
print(x.conjugate)
print(abs(x))
print(x+y)

# list

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
x.append("Guavava")
x.insert(0, "mango")
x.remove("Guavava")
x.pop()
x.sort()
x.reverse()
print(x)

print(random.randrange(1,10))
