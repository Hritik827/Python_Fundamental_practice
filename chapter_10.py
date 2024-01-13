# -----------object oriented programming--------------------------------

# This concept focuses on using reusable code------implemnts DRY principle

# class Number:  ---create a class
#     def sum(self):
#         return self.a + self.b

# num=Number()   ---object instantiation
# num.a=12
# num.b=24
# s=num.sum()
# print(s)






# class:blueprint/template
# object: instantitate object using class

# class Employee:
#     method & variable                                                EmployeeName -->pascal case

# example_1


# class RailwayForm:
#     formtype="RailwayForm"
#     def printData(self):
#         print(f"name is {self.name}")
#         print(f"name is {self.train}")

# harryApplication =RailwayForm()   #create object --instanteous harry application
# harryApplication.name="harry"     #insart data --add data
# harryApplication.train="hritik express"

# harryApplication.printData() #run thus method

# ---------------------------------------------------------------------------------------------------------------------------------------
# to create a object:-
# ek variable name=class_name ()

# -------------------------------------------------------------------------------------
# Abstraction
# implementation detail are hide from user
# user doesnot have to bodar

# encapsulation:
# biding code and data together
# ex:all player method player mein baand kar diya

# ---------------------------------------------------------------------------------------------------

# Noun-- class--- Employee
# Adjective-- attributes -- name,age,salary
# verb-- methods -- getsalary(),increament()

# attritude:properties

# class attribute:attribute belong to class
# instance attribute:attribute belong to instance

# SELF
# Self asa ek argument hai jo pass hota jab object ko automatically  call karte ho tab

# static method --special functio to modify the function
#syntax:  @staticmethod
# no need for self for static method

# constructor
# __init__() is a special method which is first run as sooon as the object is created
# it take self agrument or more argument



# Problem
# 1.

# class Programmer:
#     company="Google"

#     def __init__(self,name,product):
#         self.name=name
#         self.product=product
    
#     def getInfo(self):
#         print(f"the name of the {self.company} programmer is {self.name} and product is {self.product}")


# harry=Programmer("harry","Skype")
# alka=Programmer("alka","Gitthub")

# harry.getInfo()
# alka.getInfo()


# 2.
# class Calculator:
#     def __init__(self,num):
#         self.num=num

#     def square(self):
#         print(f"the value of {self.num} square is {self.num **2}")

#     def squareroot(self):
#         print(f"the value of {self.num} square root is {self.num **0.5}")

#     def cube(self):
#         print(f"the value of {self.num} cube is {self.num **3}")

# # a=Calculator(3)   ------- calculate class inistant or oject create
# a.square()
# a.cube()
# a.squareroot()

# 3.

# class Sample:
#     a = "Harry"

# obj = Sample()
# obj.a="Raj"

# print(Sample.a)
# print(obj.a)

# class attritubute does not change


# 4.

# class Calculator:
#     def __init__(self,num):
#         self.num=num

#     def square(self):
#         print(f"the value of {self.num} square is {self.num **2}")

#     def squareroot(self):
#         print(f"the value of {self.num} square root is {self.num **0.5}")

#     def cube(self):
#         print(f"the value of {self.num} cube is {self.num **3}")

#     @staticmethod
#     def greet():
#         print("*******welcome to the best calculator***************8")

# a=Calculator(3)  
# a.greet() 
# a.square()
# a.cube()
# a.squareroot()



#  5.
# class Train:
#     def __init__(self,name,fare,seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
    
#     def getStatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The seat available in the train is {self.seats}")

#     def fareInfo(self):
#         print(f"The price of the ticket is:Rs {self.fare}")

#     def bookTicket(self):
#         if(self.seats>0):
#             print(f"your ticket has been booked! your seat number is {self.seats}")
#             self.seats = self.seats - 1

#         else:
#             print("Sorry no ticket available! kindly book in tatkal")

#     # def cancelTicket(self):

# ticket=Train("indian express",3000,100)
# ticket.getStatus()
# ticket.bookTicket()
# ticket.bookTicket()
# ticket.getStatus()
        

# 6  
#
# class Sample:

#     def __init__(harry,name):
#         harry.name= name

# obj = Sample("hritik")
# print(obj.name)

# answer:we can change self with any name and it will be work
