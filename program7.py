
def check(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
result = check(num1, num2)
if result:
    print("✅ The condition is True (either one is 10 or their sum is 10).")
else:
    print("❌ The condition is False.")