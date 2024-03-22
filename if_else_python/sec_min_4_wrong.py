a=int(input("A is: "))
b=int(input("B is: "))
c=int(input("C is: "))
d=int(input("D is: "))
if(a<b):
    m1=b
    sm1=a
else:
    m1=a
    sm1=b
if(c<d):
    m2=d
    sm2=c
else:
    m2=c
    sm2=d
if(m1<m2):
    if(m2<sm1):
        print("sec_min  is: ",m2)
    else:
        print("sec_min  is: ",sm1)
elif(m1<sm2):
    print("sec_min  is: ",m1)
else:
    print("sec_min  is: ",sm2)