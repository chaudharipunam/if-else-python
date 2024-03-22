a=int(input("A is: "))
b=int(input("B is: "))
c=int(input("C is: "))
d=int(input("D is: "))
if(a>b):
    m1=a
    m2=b
else:
    m1=b
    sm1=a
if(c>d):
    m2=c
    sm2=d
else:
    m2=d
    sm2=c
if(m1>m2):
    if(m2>sm1):
        print("sec_max is: ",m2)
    else:
        print("sec_max is: ",sm1)
elif(m1>sm2):
    print("sec_max is: ",m1)
else:
    print("sec_max is: ",sm2)