def integerCheak(data_type):
    def outer_warper(fun):
        def inner_warper(*args):
            if type(args[0])==data_type:
                fun(*args)
            else:
                raise TypeError('invailid data type')
        return inner_warper
    return outer_warper


@integerCheak(int)
def square(num):
    print(num**2)
    
square(5)
    