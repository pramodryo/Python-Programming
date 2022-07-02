# Q1_ create a class C2d vector and use it to creat another class representing a 3-D vector

class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)




# Q2_ create a class pets from a class animals and ferther create class dog from pets. add a method bark to class dog

class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")

d  = Dog()
d.bark()



# Q3 create a class Employee and add salary and increment properties to it.
#  write a method salary after increment method with a @ property decoder with a 
# setter which change the value of increment based on the salary.


# salaryAfterIncrement =  salary * increment

class Employee:
    salary = 1000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)




# Q4_ write a class complex to represent complex number along with overload opertats + and * which add and multiples them


# (a+bi)(c+di) = (ac−bd) + (ad+bc)i

class Complex:
    def __init__(self, r, i):
        self.real = r 
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)
    
    def __mul__(self, c):
        mulReal =  self.real*c.real - self.imaginary*c.imaginary
        mulImg =  self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1 = Complex(1, -4)
c2 = Complex(331, -37)
print(c1 + c2)
print(c1 * c2)




#  Q5 write a class vector representing a vector of n diamention.
# overload the + and * operator which adds and multiple them.



class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1+v2)
print(v1*v2)


# Q6 write __str__() methos to print the vector.

class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
 

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)





# Q7 overwrite the __len__() method on vector of problem 5 
# to display the diamention of the vector

class Vector:
    def __init__(self, vec):
       self.vec = vec
    
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 6])
v2 = Vector([1, 6, 9])
print(len(v1))
print(len(v2))




