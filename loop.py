#Q1_ write a program to print the multiplication table of given number using for loop


num = int(input("Enter the number\n"))
for i in range(1, 11):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")



# Q2_ write a program to greet all the person who name start with "s" present in the list


l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)


#Q3_ write a program to print the multiplication table of given number using while loop


num = int(input("Enter the number: "))
i = 1
while i<=10:
    print(f"{num}x{i} = {num*i}")
    i = i+1



# Q4 write a program whether given number prime or not

num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")


# Q5 write a program to find sum of n natural numbers using while loop

num = int(input("enter the number "))
i = 0
sum = 0
while i<=num:
    sum = sum + i
    i = i + 1
print(sum)


# Q6 write a program for factorial calulation of numbers
# n! = 1 X 2 X 3 X ..... X n
# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")



# Q7 write a program to print "*" in the following pattren 
#    *  
#   ***
#  *****
n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))



