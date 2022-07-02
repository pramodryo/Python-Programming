# Q1 write a program to find out largest number among three number

def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))

m2 = maximum(874, 896, 852)
print("The value of the maximum is " + str(m2))


# Q2_ write a program to covert celcious to fahreheit

def farh(cel):
    return (cel *(9/5)) + 32

c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))


# Q3_ who do you prevent a python print function to print the new line at the end

print("Hello!", end=" ")
print("How", end=" ")
print("are", end=" ")
print("you?", end=" ")





# Q4_ print star pattern program

def star_print(num):
  for i in range(num):
      print("*" * (num-i)) # Prints * n-i times

num= int(input("Enter your number: "))
star =star_print(num)






# Q6_ write a program to convert inches into cms

#Note: 1 inche is equal to 2.54 cm

def formula(n):
    return n * 2.54

n = int(input("Enter the value of inches: "))
CMS = formula(n)
print(CMS)





# Q7_ write a python function multiplication table of given number


def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

num = int(input("Enter your number: "))
mul_table = table(num)
    

#  using while loop 



# def table(num):
#     i = 1
#     while i<=10:
#         print(f"{num} x {i} = {num*i}")
#         i = i+1

# num = int(input("Enter your number: "))
# mul_table = table(num)






# Q8 write a program to create a formula of (a+b)^2 and find value

def formula(a , b):
    return a*a + b*b + 2*a*b



a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
trio = formula(a,b)
print(trio)