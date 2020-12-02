#day 1 part 1

expenseReport = set(open("input.txt").read().split()) 

for entry in expenseReport:
    numA = int(entry)
    numB = 2020 - numA
    if str(numB) in expenseReport: 
        print(numA * numB)