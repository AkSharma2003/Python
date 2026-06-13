# finlay will executed anywhere if exept triger or else triger

# throw else
try:
    f=open('sample.txt','r')
except FileNotFoundError:
    print('file is missing')
except Exception:
    print('somthing went wrong')
else:
    print(f.read())
finally:
    print('finaly will executed any how')
    
    
# throw except
try:
    f=open('sample1.txt','r')
except FileNotFoundError:
    print('file is missing')
except Exception:
    print('somthing went wrong')
else:
    print(f.read())
finally:
    print('finaly will excuted anyhow')