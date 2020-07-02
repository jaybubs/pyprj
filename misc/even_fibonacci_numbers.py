def fib(x,y):
    z = x+y
    return(z)

def evens():
    x=1
    y=1
    d=0
    sm=0
    while d<4000000:
        d=fib(x,y)
        print('x: '+str(x)+' y: '+str(y)+' d: '+str(d))
        if d%2==0:
            sm+=d
            print('i summed here: ' +str(sm))
        x=y
        y=d
    return(sm)

print(evens())
