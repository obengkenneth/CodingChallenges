dolphinFirstScore = int(input("Enter dolphin's first score : "))
dolphinSecondScore = int(input("Enter dolphin's second score : "))
dolphinThirdScore = int(input("Enter dolphin's third score : "))

dolphinAverageScore = (dolphinFirstScore + dolphinSecondScore + dolphinThirdScore)/ 3
print(dolphinAverageScore)


koalasFirstScore = int(input("Enter koalas' first score : "))
koalasSecondScore = int(input("Enter koalas' second score : "))
koalasThirdScore = int(input("Enter koalas' third score : "))

koalasAverageScore = (koalasFirstScore + koalasSecondScore + koalasThirdScore)/ 3
print(koalasAverageScore)
if dolphinAverageScore >= 100 and koalasAverageScore >= 100:
    if dolphinAverageScore > koalasAverageScore:
        print("The dolphins won!")
    elif dolphinAverageScore == koalasAverageScore:
        print("It is a draw!")
    else:
        print("The Koalas won!")
else:
    print("No team wins the trophy!")

