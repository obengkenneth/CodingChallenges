markWeight = float(input("Enter Mark's  weight : "))
markHeight = float(input("Enter Mark's height : "))

markBmi = markWeight / (markHeight ** 2)
print(markBmi)

johnWeight = float(input("Enter John's weight : "))
johnHeight = float(input("Enter John's height : "))
johnBmi = johnWeight / (johnHeight ** 2)
print(johnBmi)

markHigherBmi = True if markBmi > johnBmi else False
print("Mark's bmi is higher than John's!" if markHigherBmi == True else "John's BMI is higher than Mark's!")


if markBmi > johnBmi:
    print(f"Mark's BMI({markBmi}) is higher than John's({johnBmi})")
else:
        print(f"John's BMI({johnBmi}) is higher than Mark's({markBmi})")
