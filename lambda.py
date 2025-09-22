add = lambda x, y: x + y
print(add(10, 100))

# using lambda with higher order functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# using lambda to cube a list
cube = list(map(lambda x: x**3, numbers))
print(cube)

# using lambda to find even nums in a list
even_nums = list(filter(lambda x: x%2 == 0, numbers))
print(even_nums)
