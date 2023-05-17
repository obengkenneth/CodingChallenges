billValue = int(input("Please enter the bill value : "))

tipPercent = 15/100 if 50 <= billValue <= 300 else 20/100
tip = billValue * tipPercent
finalValue = billValue + tip
print(f'The bill is {billValue}, the tip is {tip} and the total value is {finalValue}')
