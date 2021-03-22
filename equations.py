
def exponent (x):
    i=1
    e=1
    temp=1
    a=1

    while i<100:
        temp=temp*x
        a=a*i
        e=e+temp/a
        i=i+1
    return e
#print(exponent(x))
    
def Ln (x):
    if x==0:
        return 0
    if x<0:
        x= x*-1
    y= 1
    i= 0
    
    while i<100:
        y=y+2*((x-exponent(y))/(x+exponent(y)))  
        i=i+1
    return y
#print (Ln (x))

def XtimesY (x,y):
    if x==0:
        return 0
    if x<0:
        return 0
    Hezka = exponent(y*Ln(x))
    return Hezka

#print (XtimesY(x, y))
#B
def sqrt (x,y):
    if (y<=0) and (x%2==0):
        return 0
    b = exponent((1/x)*(Ln (y)))
    return b
#print (sqrt(x, y))

#C
def calculate (x):
    if x==0:
        return 0    
    calculator = exponent(x)*XtimesY(7,x)*(1/x)*sqrt(x,x)
    calculator = float('%0.6f' % calculator)
    return calculator
#print (calculate(x))

    
        
    

    
    