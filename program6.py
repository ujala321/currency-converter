def calculate(a, b):
    if a< 0 or b < 0:
        return 0
    elif a==b:
        return a+ b
    else:
        return 0
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
result = calculate(x,y)
print(f"Result:{result}")


