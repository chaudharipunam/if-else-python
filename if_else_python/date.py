y=int(input("enter the year num: "))
d=int(input("enter the day num: "))
m=int(input("enter the month num: "))
if(y>0):
    if(d>=1 and d<=31):
        if(m>=1 and m<=12):
            print("it is valid date")
        else:
            print("it is invalid date")
    else:
        print("it is invalid date")
else:
    print("it is invalid date")
