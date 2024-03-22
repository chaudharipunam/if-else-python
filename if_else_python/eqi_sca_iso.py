s1=int(input("Side1 is: "))
s2=int(input("Side2 is: "))
s3=int(input("Side3 is: "))
if(s1==s2==s3):
    print("it is Equilateral triangle")
elif(s1==s2 or s2==s3 or s1==s3):
    print("it is Isoceles triangle")
elif(s1!=s2!=s3):
    print("it is Scelene triangle")