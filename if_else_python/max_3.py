a=int(input("A is: "))
b=int(input("B is: "))
c=int(input("C is: "))
if(a>b):
    if(a>c):
        print("max is: ",a)
    else:
        print("max is: ",c)
elif(b>c):
    print("max is: ",b)
else:
    print("max is: ",c)