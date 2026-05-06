import random
randumNumber=random.randint(1,100)
print("Jackprt Number Gussing You have only 5 chance: ")
i=5
while 1<=5:
    userNumber=int(input("Enter a number: "))
    i+=1
    if userNumber==randumNumber:
        print("10 crore")
        break
    elif userNumber<randumNumber:
        print("Your number is less than Jackport Number")
    else:
        print("Your number is grater than Jackport Number")
else:
    print("Limit exised")
    print("You loos the game")