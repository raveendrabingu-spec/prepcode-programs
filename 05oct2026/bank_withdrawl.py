balance=int(input())
withdrawal=int(input())
if withdrawal<=balance:
    print(withdrawal//500)
else:
    print("no balance")