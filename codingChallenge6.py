bill = int(input("Enter the bill : "))


def calcTip(bill):
    tipPercent = 15/100 if 50 <= bill <= 300 else 20/100
    tip = bill * tipPercent
    return tip
 
tipValue = calcTip(bill)
finalValue = bill + tipValue
tips = {bill : calcTip(bill)}

total = {bill : finalValue}
print(total)