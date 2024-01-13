  # dict={
#     "hritik":"travelex",
#     "brock":"wwe",
#     "marks":[1,34,55],
#     "new_dict":{"smit":"karate","sharang":"volleyball"}
# }
# dict["marks"]=[54,76]
# print(dict["marks"])
# print(dict["new_dict"]["smit"])

# methods
# dict.keys() --> print all the keys
# dict.values() --> print all the values
# dict.items()  --> return dictionary in list format--> prints the (key,value)  for all content of the dictionary
# dict.update(dictinary_daalo_new)  --> to update the dictionary -->update the dictionary by adding key value pair 

# difference kya hai
# print(dict.get("brock2")) --> return None as brock2 is not present in dict
# print(dict("brock2"))  -->throws an error as brock2 is not present in dict




# Set(collection of non repititive element)

# a={1,2,3,5}   is a set
# set does not contain duplicate value if you put it will be remove.

# a={ }   imp: this syntax will create an empty dictionary and not empty set

# An empty set can be created using below syntax
# a=set()   --empty Set

#cannot add list and dict into set as list and dict can be change as set cannot be change


# methods
# a.add(4)  --adding value to empty set (er cannot add item repitatively)
# a.len(s)   --prints the length of this set
# a.remove(8)  --remove 5 ,if value does contain in the set if u want to remove that we will received error
# a.pop()    --remove the random value
# s.clear()  --clear the ser
# s.union({1,2})
# s.intersection({1,2})
 

#  Practice
# 1.
# dict={"bhaag":"run","ghar":"house","bhai":"brother"}
# print("option  are ",dict.keys())
# a=input("enter the hindi word\n ")
# print("the translation is:" , dict[a])

# or
# if we use get it does not show error if value is not present in dictionary

# print("the translation is:" , dict.get(a))



# 2.
# num1=int(input("enter number 1\n"))
# num2=int(input("enter number 2\n"))
# num3=int(input("enter number 3\n"))
# num4=int(input("enter number 4\n"))
# num5=int(input("enter number 5\n"))
# num6=int(input("enter number 6\n"))
# num7=int(input("enter number 7\n"))
# num8=int(input("enter number 8\n"))


# s={num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)


# 3.

# s={18, "18"}
# print(s)

# 4.   --note 20 and 20.0 as value is same is count as 1
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))


# 5.
# s={}   --dictionary
# print(type(s))


# 6.
# favlang={}
# a=input("enter your fav lang\n")
# b=input("enter your fav lang\n")
# c=input("enter your fav lang\n")
# d=input("enter your fav lang\n")

# favlang["hritik"]=a
# favlang["smit"]=b
# favlang["raj"]=c
# favlang["swapnil"]=d

# print(favlang)


# 7.
favlang={}
a=input("enter your fav lang\n")
b=input("enter your fav lang\n")
c=input("enter your fav lang\n")
d=input("enter your fav lang\n")

favlang["hritik"]=a
favlang["smit"]=b
favlang["smit"]=c
favlang["swapnil"]=d

print(favlang)


# 8. does not affect the output value unique does not get affected


# 9.
# s={8,7,12,"Harry",[1,2]}     --we cannot access set and tuple as it is unhashable 
# print(s)