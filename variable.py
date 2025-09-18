def myFunc():
    global x 
    x = "python"
    print("Hello from",x)
myFunc()
print("hello from", x)

y = "hanif"

def myFunc2():
    global y
    y = "Muhammad Hanif"
    print("Hi", y)
myFunc2()