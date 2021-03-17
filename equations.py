x= float(input("Enter num x:"))
y= float(input("Eneter num y: "))

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
    
def Ln (x):
    if x==0:
        return 0
    if x<=0:
        return 0
    y= 1
    i= 0
    
    while i<100:
        y=y+2*((x-exponent(y))/(x+exponent(y)))  
        i=i+1
    return y

def XtimesY (x,y):
    if x==0:
        return 0
    Hezka = exponent(y*Ln(x))
    return Hezka

#B
def sqrt (x,y):
    if (y<=0) and (x%2==0):
        return 0
    b = exponent((1/x)*(Ln (y)))
    return b

#C
def calculate (x):
    calculator = exponent(x)*XtimesY(7,x)*(1/x)*sqrt(x,x) 
    return calculator

    
        
    

    
    