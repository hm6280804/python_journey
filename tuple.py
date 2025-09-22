thisTuple = ("apple", "banana", "apricot")
# thisTuple[0] = "apricots"
# print(len(thisTuple))
# print(type(thisTuple))

# print(thisTuple[0])
# if "apple" in thisTuple:
#     print("yes present ")

# for x in thisTuple:
#     print(x)

# for i in range(len(thisTuple)):
#     print(thisTuple[i])
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1


# join tuples 
tuple1 = ("hanif", "shayan", "sudais")
tuple2 = (1, 3, 5)

tuple3 = tuple1 + tuple2
print(tuple3)

# count mehtod wiht tuple
numberss = (1, 3, 7, 8, 7, 5, 4, 6, 5, 5, 5)
print(numberss.count(5))

# the index method 

print(numberss.index(3))
