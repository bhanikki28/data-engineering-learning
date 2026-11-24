bill_amount = input("Please provide bill amount ")
try:
    bill_amount_fl = float(bill_amount)
except ValueError:
    print("Bill amount can't be text")
    bill_amount_fl = 0

tip_percentage =  input("Please provide tip  percentage ")
try:
    tip_percentage_fl = float(tip_percentage)
except ValueError:
    print("Tip percentage can't be String")
    tip_percentage_fl = 0.0


no_of_person = input("Enter no of person: ")
try:
    no_of_person_int = int(no_of_person)
except ValueError:
    print("No of persons can't be String")
    no_of_person_int = 1

tip_amount = bill_amount_fl * tip_percentage_fl / 100
total_amount = bill_amount_fl + tip_amount
per_person = total_amount/ no_of_person_int

print(f"The total no of person is {no_of_person_int} and bill amount is {bill_amount_fl} and tip percentage is {tip_percentage_fl}")
print(f"Total amount to be paid, including tip is {total_amount:.2f}")
print(f"Share per person is {per_person:.2f}")