


markWeight = 78
markHeight = 1.69

markBmi = markWeight / (markHeight ** 2)
print(markBmi)

johnWeight = 92
johnHeight = 1.95
johnBmi = johnWeight / (johnHeight ** 2)
print(johnBmi)

markHigherBmi = True if markBmi > johnBmi else False
print(markHigherBmi)
