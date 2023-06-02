#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5       
#taking input
v1= int(input("enter number: "))
v2 = int(input("enter number: "))


#conditions to check the value are equal
if v1==v2 or v1+v2==5 or abs(v1-v2)==5:
    print('true')
else:
    print('False')
