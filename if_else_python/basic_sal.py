bs=int(input("basic_salary is: "))
if(bs<=10000):
    HRA=20/100
    DA=80/100
    GS=bs+(bs*HRA)+bs*DA
    print(GS)
elif(bs<=20000):
    HRA=25/100
    DA=90/100
    GS=bs+(bs+HRA)+bs*DA
    print(GS)
elif(bs>20000):
    HRA=30/100
    DA=95/100
    GS=bs+(bs*HRA)+bs*DA
    print(GS)
else:
    print("INVALID")