row = {"name": "Asha", "age": 121, "state": "VIC"}
age = row["age"]

if age is None:
    print("Missing Age")
elif age < 0 or age > 120:
    print("invalid age")
else:
    print("ok")