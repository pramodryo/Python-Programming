# Q1_ write a program to find gretest number which is enterd by user

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")



 # also you can find without if else statment by following 
# list=[num1, num2, num3, num4]
# print(list)

# print("gretest number is" ,max(list))



# Q2_ write a program to find out whether student pass or fail.

sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")




# Q3_ find out spam comment which contain following word in it
# words are: "make a lot of money","buy now"," click this", "subscribe now"

text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")



# Q4_ write a program to find out whether a given your name contain 10 caractor or not?


username = input("Enter your Username: ")



if(len(username) == 10):
    print("username is correct")

else:
    print("plese enter valid username")



# Q5_ write a program which find out whether given name is present in list or not?

names = ["harry", "shubham", "rohit", "rohan", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")




# Q6_ write a program to calculate the grade of student from his marks ?

marks = int(input("Enter Your Marks\n"))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)





# Q7_ write a program to find out given post is about "harry" or not?

post = input("Enter your post\n")

if ("harry" in post):
    print("Yes! this post is about harry")
else:
    print("No! this post is not about harry")