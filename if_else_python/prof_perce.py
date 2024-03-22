sp=int(input("selling price: "))
cp=int(input("cost price: "))
if(sp>cp):
    p=sp-cp
    percent=p/cp*100
    print(percent)
else:
    print("invalid")