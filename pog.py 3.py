#Write a Python program to get the Fibonacci series of given range.

n = int(input("enter number: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
