a=int(input("A is: "))
b=int(input("B is: "))
c=int(input("C is: "))
d=int(input("D is: "))
e=int(input("E is: "))
if(a>b):
    m1=a
else:
    m1=b
if(c>d):
    m2=c
else:
    m2=d
if(m1>m2):
    if(m1>e):
        print("max is: ",m1)
    else:
        print("max is: ",e)
elif(m2>e):
    print("max is: ",m2)
else:
    print("max is: ",e)