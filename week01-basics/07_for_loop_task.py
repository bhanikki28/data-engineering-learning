number = int(input("Please enter the number: "))
print(f"The number entered is {number}")
for i in range(1, 11):
    print(i*number)


scores = [78, 92, 45, 88, 61]
total = 0
for score in scores:
    total += score
print(f"The total score is {total}")
print(f"The average score is {total/len(scores)}")


## Iterating through rows

rows = [
    {"name": "Asha", "age": 30},
    {"name": "Ravi", "age": None},
    {"name": "Mei", "age": 130},
    {"name": "Tom", "age": -2},
    {"name": "Lena", "age": 45},
]

ok_count = 0
missing_count = 0
invalid_count = 0

for row in rows:
    age = row["age"]
    if age is None:
        print(f"{row['name']}: missing age")
        missing_count += 1
    elif age < 0 or age > 120:
        print(f"{row['name']}: invalid age")
        invalid_count += 1
    else:
        print(f"{row['name']}: ok")
        ok_count += 1

print(f"The total ok_count is {ok_count}, missing_count is {missing_count} , invalid_count is {invalid_count}")