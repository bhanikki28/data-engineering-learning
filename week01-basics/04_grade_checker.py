score = int(input("Please enter the score : "))
if score >= 85 and score <=100:
    print("HD")
elif score > 75 and score < 84 :
    print("D")
elif score > 65 and score < 74 :
    print("C")
elif score > 50 and score < 64 :
    print("P")
elif score < 50 :
    print("N")
else:
    print("Invalid Score")