#Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.

#taking input
v1= int(input("enter number: "))
v2 = int(input("enter number: "))
v3 = int(input("enter number: "))

#conditions to check the value are equal
if v1==v2 or v1==v2 or v2==v3:
    print("zero")
else:
    S=v1+v2+v3
    print(S)
