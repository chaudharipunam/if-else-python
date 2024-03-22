a=int(input("A is: "))
b=int(input("B is: "))
c=int(input("C is: "))
if(a>b):
    m1=a
    m2=b
else:
    m1=b
    m2=a
if(m1>c):
    if(c>m2):
        print("second max is: ",c)
    else:
        print("second max is: ",m2)
else:
    print("second max is: ",m1)