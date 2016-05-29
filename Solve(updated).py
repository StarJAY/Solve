import math

def solve():
    a=float(raw_input('Enter a='))
    b=float(raw_input('Enter b='))
    c=float(raw_input('Enter c='))
    print a,'x^2+',b,'x+',c,'=0'
    delta=(b*b)-4*a*c

    if delta<0:
        print 'No answer'
    if delta==0:
        print 'X=',-b/(2*a)
    if delta>0:
        print 'X1=',(-b+math.sqrt(delta))/(2*a)
        print 'X2=',(-b-math.sqrt(delta))/(2*a)

solve()
while (True):
    int=raw_input('Press reset to reset:')
    if int=='reset':
        solve()