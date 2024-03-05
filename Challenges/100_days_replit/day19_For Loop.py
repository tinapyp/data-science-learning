money = 10000
rate = 0.5
counter = 0

print(f"{money} ur money over 10 years at 5% APR")
for loop in range(10):
    counter += 1
    money += money * rate
    print(f"Year {counter} is {money:.2f}")
