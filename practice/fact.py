num=int(input("Enter a number: "))
result=0
fact=1
for i in range(1,num+1):
    fact=fact*i
    result=result+fact

print("Sum of all factorial up to num is",result)


