 #loops in Python

# loop==repeat more than 1

# 2 type of Loop
# 1.while
# 2.for


# Note:i=i+1

# syntax: 
# while-----------------------------------------------------------------
# while condition:
#     Body of the loop


# test
# i=0
# while i<10:
#     print("yes " + str(i))
#     i=i+1


# Quiz
# i=1
# while i<=50:
#     print(i)
#     i=i+1

# note:if the confition never become false ,the loop keeps getting executed

# Quiz:
# list using while loop  ***

# fruit=["banana","watermelon","grapes","mango"]
# i=0
# while i<len(fruit):
#     print(fruit[i])
#     i=i+1


# for--------------------------------
# iterate-->list,tuple or string

# remember: for item in list: -----------------------
# remeber : for i in range(8):------------ 0 to 7 ---------------
#remeber :for i in range(1,8):  ----------- 1to 7
# range(start,stop,step_size)

# l=[1,2,3,4,5]
# for item in l:
#     print(item)

# range function
# for i in range(1,8):
#     print(i)


# break-----------------
# Break it intent the code to exist the loop


# for i in range(1,8):
#     print(i)
#     if i==5:
#         break
                
# print("value is 5")


# continue-----------------------------------------------------------
# continue:skip that loop
# for i in range(1,8):
#     if i==5:
#         continue
#     print(i)


# pass------------------------------------------------------------------------
# do nothing means pass
# i=4
# if i>0:
#     pass
# print("hritik is the best")

# f_string-------------------------------
# when ever there is variable use { }
# example:
# print(f"{num}x{i}={num*i}")


# practice------------------------
# 1.
# num=int(input("enter a number"))
# for i in range(1,11):
#     print(str(num) + "x" + str(i) + "=" +str(num*i))
#     i=i+1


# 2
# list=["Harry","Soham","Sachin","Hritik"]
# for name in list:
#     if name.startswith("S"):
#         print(f"Welcome to the my world {name}")

# 3.
# num=int(input("enter the number"))
# i=1
# while i<=10:
#     print(f"{num} x {i} = {num*i}")
#     i=i+1

# 4.

# num=input(input("enter the number: "))
# prime=True
# for i in range(2,num):
#     if(num%i==0 ):
#         prime=False
#         break
# if prime:
#     print("this number is prime")
# else:
#     print("this number is not prime")

# 5.
# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#     sum=i+sum
#     i=i+1
# print(sum)


# 6.
# n!=1x2x3x....xn

# n=int(input("enter the number:"))
# fact=1
# for i in range(1, n+1):
#     fact=fact *i
# print(f"the factorial is {fact}")

# 8.
# n=4

# for i in range(4):
#     print("*" * (i+1))

 


# 7.
# row=3
# spaces & *
# note:  end=" " ----------------------new line print nahi karega
# n=3
# for i in range(3):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))



#9 practice


# 10.

# num=int(input("enter a number"))
# x=9
# for i in range(1,11):
#     i=i+x
#     x=x-1
#     print(str(num) + "x" + str(i) + "=" +str(num*i))
   

















                

