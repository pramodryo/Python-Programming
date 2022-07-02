# Q.1_create a calss for programmer for soring information of few candidate who working in microsoft

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


harry = Programmer("Harry", "Skype")
alka = Programmer("Alka", "GitHub")
harry.getInfo()
alka.getInfo()





# Q.2_write a calculator capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

a = Calculator(9)
a.square()
a.squareRoot() 
a.cube()




'''Q.3_creat a class with a class attributes a; creat an object from it and set a directly using object a = 0 
 does this charge the clss attribute'''

class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"

print(Sample.a)
print(obj.a)



# Q4  Create a calss "Calculator" which calulate squre, squre root and cube.

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")
    
    @staticmethod
    def greet():
        print("*******Hello there welcome to the best calculator of the world*******")

a = Calculator(9)
a.greet()
a.square()
a.squareRoot() 
a.cube()




'''Q.5_write a class train which has method to book a ticket, get status (no. of seats) 
and get fare information of trains runnig under indian railway'''

'''
seat number: 1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        pass

intercity = Train("Intercity Express: 14015", 90, 10)
intercity.getStatus() 
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()







