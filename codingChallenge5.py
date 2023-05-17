


def calcAverage(first, second, third):
    "This is a function that finds the average of 3 numbers"
    average = (first + second + third)/ 3
    return average

avgDolphins = calcAverage(85,54, 41)
avgKoalas = calcAverage(23, 34, 27)
def checkWinner(firstAvg, secondAvg):
    "This function prints a winner if one of the parameters is at least double the value of the other parameter "
    if avgDolphins >= (2*avgKoalas):
        print(f'Dolphins win ({avgDolphins} vs {avgKoalas})') 
    elif avgKoalas >= (2*avgDolphins): 
        print(f'Koalas win ({avgKoalas} vs {avgDolphins})') 
    else: print("No team wins!")

checkWinner(avgDolphins, avgKoalas)