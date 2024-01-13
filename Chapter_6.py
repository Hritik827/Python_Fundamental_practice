# Conditional Expressions
# if else and elif in python

# syntax:
#      if(condition1):
#         print("yes")
#      elif(condition2):
#         print("No")
#     else:
#         print("Maybe")


# if -elif ladder
# multiple if statements -- all if condition will be check 

# indentation:to know next line is in if statement


# quiz
# a=int(input("enter the age"))
# if(a>=18):
#     print("yes")
# else:
#     print("no")


# Relational operator:
# ==
# <=
# >=

# logical operator:         if(age>34 and age<56):
# and
# or
# not


# is and in
# is:check value is
# in:presen in that value


# pass


# practice:

# 1.
# a=int(input("enter no 1:\n"))
# b=int(input("enter no 2:\n"))
# c=int(input("enter no 3:\n"))
# d=int(input("enter no 4:\n"))

# if(a>d):
#     f1 = a
# else:
#     f1 = d
# if(b>c):
#     f2 = b
# else:
#     f2 = c

# if(f1>f2):
#     print(str(f1) + "is greatest")
# else:
#     print(str(f2) + "is greatest")



# 2.
# sub1=int(input("enter  1:\n"))
# sub2=int(input("enter  2:\n"))
# sub3=int(input("enter  3:\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail")
# if(sub1+sub2+sub3)/3 <40:
#     print("you are fail due to total percentage less than 40")
# else:
#     print("cong!you are pass")


# 3.
# comment=input("enter text:")  --my try
# if("make a lot of money" in comment):
#     print("spam")
  
# 3

# comment=input("enter text:\n")

# if("make a lot of money" in comment):
#     spam=True
# elif("buy now" in comment):
#     spam=True
# elif("click this" in comment):
#     spam=True
# elif("subscribe" in comment):
#     spam=True
# else:
#     spam=False

# if(spam):
#     print("this text is spam")
# else:
#     print("this text is not spam")


# 4.
# a=input("enter username:\n")
# if(len(a)>=10):
#     print("username contain character more than 10")
# else:
#     print("username contain character less than 10")


# 5.
# names=["harry","hritik","rohan","raj"]
# name=input("Enter the name to check\n:")
# if(name in names):
#     print("name is present in the list")
# else:
#     print("name is not present in the list")

# 6.
# marks=int(input("enter your marks\n:"))
# if marks>=90:
#     grade="Ex"
# elif marks>=80:
#     grade="A"
# elif marks>=70:
#     grade="B"
# elif marks>=60:
#     grade="C"
# elif marks>=50:
#     grade="D"
# else:
#     grade="F"
# print("your marks are:" , grade)


7.
post=input("enter the post:\n")
update_post=post.lower()
if("harry" in update_post):
    print("harry is present the post")
else:
     print("harry is not present the post")