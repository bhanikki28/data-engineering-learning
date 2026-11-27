transactions = [
    {"category": "food", "amount": 20},
    {"category": "travel", "amount": 150},
    {"category": "food", "amount": 35},
    {"category": "bills", "amount": 90},
    {"category": "food", "amount": 12},
]
count ={}
totals ={}
for transaction in transactions:
    category = transaction["category"]
    amount = transaction["amount"]

    if category in count:
        count[category] += 1
    else:
        count[category] = 1

    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

print(count)
print(totals)
