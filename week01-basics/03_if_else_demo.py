number = int(input("Please enter the number to check whether it is odd or even: "))
remainder = number % 2 
if remainder == 0:
    print(f"The given no {number} is Even")
else:
    print(f"The given no {number} is Odd")