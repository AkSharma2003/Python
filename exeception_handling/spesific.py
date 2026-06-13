try:
    m=5
    f=open('sample.txt','r')
    print(f.read())
    print(m)
    print(5/0)
    L=[1,2,3,4]
    L[100]
except FileNotFoundError:
    print("file is not founded")
except ZeroDivisionError:
    print("you cant diide by zero")
except NameError:
    print('variable not defiend')
except Exception as e:
    print(e)

    