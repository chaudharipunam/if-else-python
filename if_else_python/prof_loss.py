sp=int(input("selling price: "))
cp=int(input("cost price: "))
if(sp>cp):
    profit=sp-cp
    print("profit")
elif(cp>sp):
    loss=cp-sp
    print("loss")
elif(cp==sp):
    print("equal")
