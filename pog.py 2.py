#Write a Python program to get the Factorial number of given number.    

n=int(input('Enter number: '))
f=1
for i in range(1,n+1):
    f= f*i
    print(f"factorial of {n} is {f}")
