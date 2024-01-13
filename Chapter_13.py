# Chapter 13---------------------------------------------------------------
# Virtual Environment 
# note: two term system interpreter and virtual interpreter


# Package:pip install virtualenv
# virtualenv myprojectenv  --create a virtual environment

# to use we have to activate----------------
# if i write mypro and then type TAB ye auto complete karega

# .\myprojectenv\Scripts\activate.ps1 -------to activate

# whatever will be install using pip will be install in virtual enivornment

# to deactivate virtual environment----------------
# deactivate


# all package present on that particular environement---
#  pip freeze


# create a txt file by name requirement.txt and put all freeze value inside that along with version---------------
# pip freeze > requirements.txt  


# we can recreate the same requirement using:--------
# #  pip install -r .\requirements.txt 
# note: give this txt file to other user and enter this code



# lambda--------------


# Syntax:
# lambda arguments:expressions--> can be used as a normal function

# Ex:
# Square=lambda x: x*x
# Square(6)


# join--------------------(bin method)
# it is use for string to add something in between to item in the list
# create a string from ilterated object

# example:

# l=["apple","mango","banana"]
# sentence="and".join(l)
# print(sentence)


# format method------------------

# this is use before f string 

# synatax:
# .format(arguments)


# name="hritik"
# channel="codewithhritik"
# # a= f"this is my name {name}"   ----using f string

# a="This is {}".format(name)
# or

# b="This is {} and his channel is{}".format(name,channel)
# print(b)
# or
# c="This is {0} and his channel is{1}".format(name,channel)
# print(a)

# refer:notes



#map/filter and reduce-------------------------------------

# map---------
# we use it a function to apply to all the items in an list

# def Square(num):
#     return num*num

# l=[1,2,3,4]
# print(list(map(Square, l)))
# note:we have typecast the list


# filter----------

# synatax:
# list(filter(funct_name,list_name))

# def greater_than_5(num):
#     if num>5:
#         return True
#     else:
#         return False
    
# l=[1,2,3,4,5,6,7,8,9,19]
# print(list(filter(greater_than_5,l)))


# reduce------

# syntax:
# variable=reduce(function_name,List_name)

# note: we have to import reduce
# --------from functools import reduce


# reduce applies a rolling computation to sequential pair of elements

# from functools import reduce

# sum=lambda a,b: a+b
# l=[1,2,3,4]
# val=reduce(sum,l)
# print(val)



# --------------------------------------------------------------------------------------------------------------------------------

# problem1.

# open terminal
# virtualenv env1
# virtualenv env2
# .\env1\Scripts\activate.ps1
# pip install numpy pandas flask matplotlib
# pip freeze
# pip freeze >requirements.txt
# deactivate

# .\env2\Scripts\activate.ps1
# pip install -r .\requirement.txt





# problem2

# {}-->place holder
# name=input("enter you name:")
# marks=input("enter you marks:")
# phone=input("enter you phone Number:")

# template="The name of the student is {},hia marks are {} and phone number is {}".format(name,marks,phone)
# output=template.format(name,marks,phone)
# print(output)




#problem3

# note:join function is use for str so we use str(i*7)

# l=[str(i*7) for i in range(1,11)]
# print(l)

# vertical_table="\n".join(l)
# print(vertical_table)


# problem4

# l=[1,2,3,4,5,10,15,23,56,80]

# a=list(filter(lambda a: a%5==0,l))
# print(a)




# problem 5

# # note: max(10,15)  --->return max

# from functools import reduce
# l=[3,8,4,2,5]
# a=reduce(max,l)
# print(a)


# problem 6

# pip freeze
# pip freeze > req2.txt
# virtualenv hritik
# .\env1\Scripts\activate.ps1
# pip install -r .\req2.txt  ------------>req2 wale file he sarre package ye env mein create karna hai





# # problem 7

# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '''<!doctype html>
#         <html lang="en">
#         <head>
#             <!-- Required meta tags -->
#             <meta charset="utf-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

#             <!-- Bootstrap CSS -->
#             <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

#             <title>Hello, world!</title>
#         </head>
#         <body>
#             <h1>Hello, world!</h1>
#             <div class="alert alert-primary" role="alert">
#         A simple primary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-secondary" role="alert">
#         A simple secondary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-success" role="alert">
#         A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-danger" role="alert">
#         A simple danger alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-warning" role="alert">
#         A simple warning alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-info" role="alert">
#         A simple info alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-light" role="alert">
#         A simple light alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#         <div class="alert alert-dark" role="alert">
#         A simple dark alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
#         </div>
#             <!-- Optional JavaScript -->
#             <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#             <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
#             <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
#             <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
#         </body>
#         </html>'''

# if __name__ == "__main__":
#     app.run(debug=True)
