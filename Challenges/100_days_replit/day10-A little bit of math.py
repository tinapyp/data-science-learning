myBill = float(input("What was the bill?: "))
tip = float(input("how much tip u give?(%): "))
numberOfPeople = int(input("How many people?: "))
answer = (myBill + (tip * myBill)) / numberOfPeople
print("You all owe", round(answer, 2))
