# email=input("Enter email: ")
# password=int(input("Enter your password: "))

# if email=='ankit824012@gmail.com' and password==1234:
#     print("Welcome")
# else:
#     if email=='ankit824012@gmail.com':
#         password=int(input("Enter correct password:"))
#         if password==1234:
#             print("Welcome")
#     else:
#         print("please enter correct details")

# min of three number

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

if a<b:
    if a<c:
        print(a,"is min")
    else:
        print(c,"is min")
else:
    if b<c:
        print(c,"is min")
    else:
        print(b,"is min")
