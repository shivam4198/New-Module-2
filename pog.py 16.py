#Write a Python function to reverses a string if its length is a multiple of 4:

string = input("Enter a string: ")
if len(string)%4==0:;
    reverse=reversed(string)
    reverse_string="".join(reverse)
    print(reverse_string)
else:
    print('Not s multiple of 4')
