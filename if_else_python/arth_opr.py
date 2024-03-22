a=int(input("A is: "))
b=int(input("B is: "))
c=(input("C is: "))
if(c=='+'):
    n=a+b
    print(n)
elif(c=='-'):
    n=a-b
    print(n)
elif(c=='*'):
    n=a*b
    print(n)
elif(c=='/'):
    n=a/b
    print(n)
else:
    n=a%b
    print(n)