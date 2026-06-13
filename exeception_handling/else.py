try:
    f=open('sample.txt','r')
except FileNotFoundError:
    print('file is missing')
except Exception:
    print('somthing went wrong')
else:
    print(f.read())
    
    
# in the above example is except part will executed then else block cant be excute optherwise else execute

try:
    f=open('sample1.txt','r')
except FileNotFoundError:
    print('file is missing') # file is missing so else part will not trigerd
except Exception:
    print('somthing went wrong')
else:
    print(f.read())
 