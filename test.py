
import time
'''add docstring againg '''

def count(f):
    def inner(*args, **kargs):
        inner.counter += 1
        return f(*args, **kargs)
    inner.counter = 0
    return inner

@count
def my_fnc():
    pass



def timer(f):
    def inner(*args, **kargs):
        t = time.time()
        ret = f(*args, **kargs)
        print('timer = %s' %(time.time()-t))
        return ret
    return inner

@timer
def my_fnc1():
    pass

if __name__ == '__main__':
    my_fnc()
    my_fnc()
    my_fnc()
    print('my_fnc.counter=',my_fnc.counter)

    my_fnc1()