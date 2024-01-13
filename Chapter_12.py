#Advanced Python 1

# Exception Handling in python --------------------------------------------------------------------------------------
#  it is use to handle error
# it help not to crash the code because we have handle the error  
# it only kill that particular iteration
# when rge exception is handled ,the code flow continues without prgram interruption.

# syntax
# try:
#     #code
# except Exception as e:
#     print(e)     e is error enter by User
#     or
#     customice the print using f string
#     print(f"Your input resulted in an error: {e}")
    #   or 
    #   #code


#read on google:python differeny errors  

#------ handling_different_error----

# example in exception:
# Syntax:

# except ValueError as e :
# Code   
# except ZeroDivisionError as e :
# Code 

#---- Raise:the Error-----
# example in exception:
# Syntax:

# except:
#     raise ValueError("This is not good - Harry")

# ----Try with else clause----
# try:
#     Code  
# except:
#     Code  
# else:
#     Code  


#--try with finally ---
# try:
#     Code   
# except:
#     code  
# finally:   ---yr surely excecute hoga
#     code   




# if __name__=='__main__' in Python=--------------------------------------------------------------------------------------  
# if we want to use a some complex part of the  function in another code we use this method 

# note : import filename  
#        filename.function_name()

# syntax:
# if __name__=='__main__' 


# Global keyword--------------------------------------------------------------------------------------
# a=54   Global Variable
# def func1():
#     global a
    #   a=4  global variable
#     print(a)
#     # a=8 local variable if global keyword is not used 
#     print(a)

# func1()
# print(a)


# enumerate function-------------------------------------------------------------------------
# list1=[3,54,False,"hritik",6.2]
# for item in list1:
#     print(item)

# To get the item and index we use enumerate function
# list1=[3,54,False,"hritik",6.2]
# for index,item in enumerate(list1):
#     print(index,item)

# Synatax:
# for index,item in enumerate(list1):



# List Comprehensions----------------------------------------------------------------------------------
# a=[2,3,45,6,88,4,6,33,566]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)

# using list Comprehensions---
# a=[2,3,45,6,88,4,6,33,566]
# b=[i for item in a if item%2==0]
# print(b)



# Problem Set-----------------------------------------------------------------------------------------------------------------------

# 1.
# def readFile(filename):
#     try:
#         with open(filename,"r") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f"File {filename} is not found")

# readFile("1.txt")
# readFile("2.txt")
# readFile("3.txt")




# 2
# list=[1,2,3,4,5,6,7,8,9,10]
# for index,item in enumerate(list):
#     if index==2 or index==4 or index==6 :
#         print(f"The {index+1}th element is {item}")


# 3
# num=int(input("enter the number:"))

# table=[num*i for i in range(1,11)]
# print(table)


# 4.
# a= int(input("enter number a:"))
# b= int(input("enter number b:"))

# try:
#     print(a/b)
# except:
#     print("Infinite")

# 5.
num=int(input("enter the number:"))

table=[num*i for i in range(1,11)]
print(table)
with open("table.txt","a") as f:
    f.write(str(table))
    f.write("/n")