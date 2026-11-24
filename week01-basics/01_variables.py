# A variable is a name that points to a value
name = "Bharathy"          # str   (text)
age = 30                   # int   (whole number)
height_m = 1.62            # float (decimal number)
is_learning = True         # bool  (True or False)

print(name, age, height_m, is_learning)
print(type(name), type(age), type(height_m), type(is_learning))

# f-strings: put variables inside text
print(f"Hi, I'm {name} and I'm learning Python!")

# Maths operators
a = 17
b = 5
print(a + b, a - b, a * b)   # 22 12 85
print(a / b)                 # 3.4  -> normal division always gives a float
print(a // b)                # 3    -> floor division (drops the decimal)
print(a % b)                 # 2    -> remainder
print(a ** 2)                # 289  -> power

# Converting between types
price_text = "49.99"
price = float(price_text)
print(price * 2)             # 99.98

# Getting input from the user
city = input("Which city are you in? ")
print(f"{city} is a great place to learn data engineering!")