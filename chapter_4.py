# # List and Tuples
# list
# list are containers to store a set of value of same datat set
# prdered list 
# create a list using []
# print(a[0]) --> accesss 1st element or a[1],a[2]
# a[0] =98  --> changes the elemet value

# we can create a list with items of different types
# a=[45,"harry",False,6.9]


# slicing in list
# print(friends[0:4])

# list methods
# dont need to store in one variable l1.sort sort the l1 list directly
# l1.sort()  -->increasing order the list
# l1.reverse()  --> reverse order the list
# l1.append(8)   --> append at the  end of the list  ******************  
#  l1.insert(3,5)  --> 5 is add at index 3
#l1.pop--> remove elemet at index 3


#tuples
# creating a tuple using ( )
# t=(1,2,3,4)

# t=( ) ==> empty tuple
# t1=(1,)  ==> tuple with one element : remember ','

# note:cannot update the values of a tuple
# immutable

# tuple:immutable
# list mutable


# methods
# a.count(1) --> count 1 in the tuple
# a.index(1)  --> provide the first occurence of 1 ,also help in searching


# practice

# 1.user enter the detail in list

# f1=input("enter fruit no.1:")
# f2=input("enter fruit no.2:")
# f3=input("enter fruit no.3:")
# f4=input("enter fruit no.4:")
# f5=input("enter fruit no.5:")
# f6=input("enter fruit no.6:")

# fruit=[f1,f2,f3,f4,f5,f6]
# print(fruit)

# 2.marks and sort them
# m1=int(input("enter marks of student no.1:"))
# m2=int(input("enter marks of student no.2:"))
# m3=int(input("enter marks of student no.3:"))
# m4=int(input("enter marks of student no.4:"))
# m5=int(input("enter marks of student no.5:"))
# m6=int(input("enter marks of student no.6:"))

# marks=[m1,m2,m3,m4,m5,m6]
# marks.sort()
# print(marks)


# 3.check that tuple cannot change in python
# a=(1,2,34,5,6,7)
# a[0]=65
# hence prove

# 4.sum_a_list
# a=[1,23,455,233]
# x=a[0]+a[1]+a[2]+a[3]
# print(x)


# additing practice add 4 to each element
# a=[2,3,5,6]
# a[0]=a[0]+4
# a[1]=a[1]+4
# a[2]=a[2]+4
# a[3]=a[3]+4
# print(a)


# 5.count no of zeros
# a=(4,0,0,0,2,4,6)
# x=a.count(0)
# print(x)