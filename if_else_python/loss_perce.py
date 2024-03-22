sp=int(input("selling price: "))
cp=int(input("cost price: "))
if(cp>sp):
    l=cp-sp
    percent=l/sp*100
    print(percent)
else:
    print("invalid")