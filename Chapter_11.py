# Chapter 11 --------------------------------

# Inheritance and more on OOPs
# Inheritance is a  way of creating  a new class from an existing class  (Implementation DRY principle)
# we can override the method in child class

# Syntax:
# Class Employee:                 ------base class
#     #code

# Class Programmer(Employee):   ---------Derived or child class
#     #code


# Types of inheritance
# 1.single inheritance  -->     base class ---> derived class                      ex:Class Programmer(Employee)
# 2.muliple inheritance  -->    more than one parent class --> one child class      ex:class Programmer(Employee,Freelancer)   *****arrangment of class is another imp in between the bracket***********
# 3.multilevel inheritance -->    parent --> class1 --> class2 
# ex for multilevel
# class person:
# class Employee(person):
# class Progarmmer(Employee):              


# Super()  class
# # Super method is used to access the mmethods of a super class in the derived class
# Super()__init__()     ---> callsconstructor of the base class

# example: super().method_name() or Super()__init__()     --->write it before print statement
# in short it will take his ke upar wale class ka method


#Note:staticmethod :self is not use in the method so we can use static method

# class method-------------------------------------------------------------------------------------------
# to change the class attribute
# self.salary=salary   ---->initance attribute change
# 1 way :self.__class__.salary =salary   --->class attribute changes

# 2 way:
# @ classmethod                               --->decorate-->take function as input
# def changeSalary(cls,salary):
#     class.salary=salary

# # --------------------------------------------------------------------------------------------
# property:
# it is look like function but it is property--------->also called getter

# class Employee:
#     company="Bharat"
#     salary=5600
#     salarybonus=400
#     # totalSalary=6100   rader than doing this mannually we use the function

# @property
# def totalSalary(self):
#     return self.salary + self.salarybonus

# @totalSalary.setter
# def total.Salary(self,val):
#     self.salarybonus=val-self.salary

# # e=Employee()
# # print(e.totalSalary)
# e.totalSalary=5800
# print(e.salary)
# print(e.salarybonus)


# setter
# @ name_function.setter
# def name_function(self.value):
#     self.ename=value

# ------------------------------------------------------------------------------------------------------------------------

# Operator overloading in python

# using dunder(__add__,__mul__)


# class Number:
#     def __init__(self,num):
#         self.num=num

#     def __add__(self,num2):
#         print("Lets add")
#         return self.num + num2.num
    
#     def __mul__(self,num2):
#         print("Lets add")
#         return self.num * num2.num
# n1=Number(4)
# n2=Number(6)
# sum=n1+n2
# mul=n1*n2
# print(sum)
# print(mul)

#other dunger method-------------------------------------------------------------------

# class Number:
#     def __init__(self,num):
#         self.num=num

#     def __add__(self,num2):
#         print("Lets add")
#         return self.num + num2.num
    
#     def __mul__(self,num2):
#         print("Lets add")
#         return self.num * num2.num
    
#     def __str__(self):
#         return f"Decimal number:{self.num}"
    
#     def __len__(self):
#         return 1
    
# n=Number(9)
# print(n)
# print(len(n))
# refer:notes

# ------------------------------------------------------------------------------------------------------------------------------------

# 1.
# class C2dVec:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j

#     def __str__(self):
#         return f"{self.icap}i +{self.jcap}j"

# class C3dVec(C2dVec):
#     def __init__(self, i, j, k ):
#         super().__init__(i, j)
#         self.kcap=k

#     def __str__(self):
#         return f"{self.icap}i +{self.jcap}j+{self.kcap}k"
    
# V2d=C2dVec(1,3)
# V3d=C3dVec(1,9,7)
# print(V2d)
# print(V3d)

# 2.
# class Animal:
#     animalType="Mammal"

# class Pets:
#     color="White"

# class Dog:
#     @staticmethod                   self use nahi karega so static method
#     def bark():
#         print("Bow Bow!")

# d=Dog()
# d.bark()


# 3.
#salaryAfterIncrement= salary*increment

# class Employee:
#     salary=1000
#     increment=1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#         self.increment=sai/self.salary

# e=Employee()
# print(e.salaryAfterIncrement)
# print(e.increment)
# e.salaryAfterIncrement=2000
# print(e.increment )

# 4
# (a + ib) (c + id) = (ac - bd) + i(ad + bc)
# class Complex:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i

#     def __add__(self,c):
#         return Complex(self.real +c.real,self.imaginary+c.imaginary)
    
#     def __mul__(self,c):
#         mulReal= self.real*c.real - self.imaginary*c.imaginary
#         mulImg= self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal,mulImg)
    
#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real}-{-self.imaginary}"
#         else:
#             return f"{self.real}+{self.imaginary}i"

#         # or use this is basic return which dont check anything return f"{self.real}+{self.imaginary}i"


# c1=Complex(1,4)
# c2=Complex(8,5)
# print(c1+c2)
# print(c1*c2)




# 5.
# class Vector:
#     def __init__(self,vec):
#         self.vec=vec

#     def __str__(self):
#         str1=""
#         index=0
#         for i in self.vec:
#             str1 +=f"{i}a{index} +"
#             index+=1
#         return str1[:-1]
    
#     def __add__(self,vec2):
#         newList=[]
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)
    
#     def __mul__(self,vec2):
#         sum=0
#         for i in range(len(self.vec)):
#             sum+=(self.vec[i] + vec2.vec[i])
#         return sum
    
# v1=Vector([1,4,6])
# v2=Vector([1,6,9])
# print(v1+v2)
# print(v1*v2)

# 6

# class Vector:
#     def __init__(self,vec):
#         self.vec=vec

#     def __str__(self):
#         return f"{self.vec[0]}i+{self.vec[1]}j+{self.vec[2]}k"
    
# v1= Vector([1,4,6])
# v2=Vector([1,6,9])
# print(v1)
# print(v2)


# 7.

class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 +=f"{i}a{index} +"
            index+=1
        return str1[:-1]
    
    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum+=(self.vec[i] + vec2.vec[i])
        return sum
    
    def __len__(self):
        return len(self.vec)
    
v1=Vector([1,4,6])
v2=Vector([1,6,9])
print(len(v1))
print(len(v2))