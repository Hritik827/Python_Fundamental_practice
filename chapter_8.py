# function
# a grp of statment perform specific task
# to reuse the code again

# ex:
# def percent(marks):
#     p= ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
#     return percentage

# mark1=[45,56,77,87]
# percentage=percent(mark1)

# print(percentage)

# remember--------------------------------
# definiting********************** may or may not take argument
# return**
# call**


# quiz
# def greet(name):
#     return print(f"good morning! {name}")

# name=input("enter your name")
# greet(name)


# type of function
# 1.build in function
# 2.user defined function


# note:
# default parameter Value
# def greet(name="stanger"):
# sranger will be taken when no parameter will be pass


# --------------------------------------------

# recursion:function calling itself

# n!=1 x 2 x 3 x4.. X n
# n!=(n-1)! X n

# using function----------------------------------------------------------------------------------------------------------
# def fact(n):
#     product=1
#     for i in range(n):
#         product=product * (i+1)
#     return product
# # f=fact(5)
# print(f)

# using recurrsion---------------------------------------------------------------------------------------------------------
# def fact_rec(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * fact_rec(n-1)
# # f=fact(5)
# f=fact_rec(1)
# print(f)



# practice
# 1.
# def max(num1,num2,num3):
#     if(num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m=max(1,2,3)
# print("the value max is:", str(m))



# 2.
# def farh(c):
#     return (c*(9/5)) + 32 
    
# c= 45
# f=farh(c)
# print("fahreheit temp is" +str(f))



# 3
# print("hello", end=" ")
# print("hi", end=" ")
# print("huu", end=" ")
# print("aa", end=" ")

# bydefault \n astaa print value


# 4.
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n +sum(n-1)
    
# n=4
# result=sum(4)
# print(f"the sum of n natural number :  {result}")


# 5.
# n=6
# for i in range(n):
#     print("*" * (n-i))  #print * from n- i times


# 6.
# def convert(inches):
#     if inches==1:
#         return 2.54
#     else:
#         return (inches*(2.54))
# n=5   
# result= convert(n)
# print(f"{n} inches = {result}cm")
    
# 7.
# strip function remove extra space 
def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()


this="     Harry is a good boy     "
n=remove_and_strip(this, "Harry")
print(n)


# 8.  --------------try-------- remove
# def mult_table(n):
#     for i in range(10):
#         result=(i+1) * n
#         return result
    
# n=5
# table=mult_table(n)
# print(table)
# # # print(f"{n} x{i}= {table}")






