#pick a prime number in python
# first way
# num = 29

# take input from user
num = int(input("Enter a number: "))

#define a flag variable
flag = False

# prime numbers > 1

if num > 1:
    for i in range(2, num):
        if(num % 1) == 0:
            flag = True
            break

#check if 'flag' is True
if flag:
    print(num, " is not a prime number.")
else: 
    print(num, " is a prime number.")


