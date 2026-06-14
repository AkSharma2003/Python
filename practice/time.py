import time

def timer(fun):
    def warp(*args):
        start=time.time()
        fun(*args)
        print('time taken by ',fun.__name__,time.time()-start,'sec') # here 'fun.__name__,time' print function original name
    return warp


@timer
def hello():
    print('hello world')
    time.sleep(2)
    
hello()


@timer
def square(num):
    print(num**2)
    
square(4)

@timer
def power(a,b):
    print(a**b)
    
power(3,4) 
    
        