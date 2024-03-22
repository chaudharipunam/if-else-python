# a=int(input("A is: "))
# b=int(input("B is: "))
# c=int(input("C is: "))
# d=int(input("D is: "))
# if(a<b):
#     m1=a
#     tm1=b
# else:
#     m1=b
#     tm1=a
# if(c<d):
#     m2=c
#     tm2=d
# else:
#     m2=d
#     tm2=c
# if(m1<m2):
#     if(m2<tm1):
#         print("3_max is: ",m2)
#     else:
#         print("3_max is: ",tm1)
# elif(m1>tm2):
#     print("3_max is: ",m1)
# else:
#     print("3_max is: ",tm2)



a = int(input("A is: "))
b = int(input("B is: "))
c = int(input("C is: "))
d = int(input("D is: "))

# Determine the maximum and minimum of A, B, C, and D
max_num = max(a, b, c, d)
min_num = min(a, b, c, d)

# Calculate the sum of the four numbers
total = a + b + c + d

# The third maximum is the difference between the total sum and the max and min values
third_max = total - max_num - min_num

print("Third maximum is:", third_max)
