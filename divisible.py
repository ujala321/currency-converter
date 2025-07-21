number = input("Enter a number: ")

if number and number[-1].isdigit():
    last_digit = int(number[-1])
    if last_digit % 5 == 0:
        print("Yes, the last digit is divisible by 5.")
    else:
        print("No, the last digit is not divisible by 5.")
else:
    print("Invalid input. Please enter a valid number.")
