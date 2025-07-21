
num = int(input("Enter a number: "))
reversed_num = 0
original = num 
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"The reverse of {original} is: {reversed_num}")