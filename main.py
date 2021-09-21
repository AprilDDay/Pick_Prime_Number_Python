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


#pick a prime number in python
# second way
num2 = int(input("Pick a number: "))

# prime numbers are greater than 1
if num2 > 1:
    for j in range(2, num2):
        if (num2 % 1) == 0:
            print(num2, " is not a prime number.")
            (print(j, " times ", num2//j, "is", num2))
        else: 
            print(num2, " is a prime number.")
else: 
    #if num2 is less than or equal to 1, it is not prime
    print(num2, " is not a prime number.")

# https://www.programiz.com/python-programming/examples/prime-number