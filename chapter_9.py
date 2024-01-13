# file I/O

# Ram:volatile,HD:non volatile

# there are 2 types of files:
# 1.Text files
# 2.Binary files


# 1.opening a File
# open("this.txt","r")   by default the mode is r


# ex:
# open("this.txt","r") --->open the file
# data=f.read()----> read its contents
# print(data)--->print its content
# f.close() **********  ---->close the file

# note:read(2)  we can also specify the number of character----> read to 2 character

# 2.other method to read the file
# readline()  -->read only one line  
# readlines()  --> read all the lines

# 3.modes of opening a File   
# r-> open in reading
# w-> open in writing
# a-> open in appending
# +-> open in updating
# rb-> open for read in binary mode
# rt-> open for read in text Mode  

# 4.writing files in python
# f=open('another.txt','w')
# f.write("please write this to the file")
# f.close()


# 5.with statment

# with open('sample.txt','r') as f:
#     a=f.read()
# print(a)

# with open('sample.txt','w') as f:
#     a=f.write("me")


# remember:

# with open("script.txt") as f:
#     content=f.read()
# with open("script.txt","w") as f:
#      f.write(content)



# # practice----------------------------------------------
# 1.
# f=open('poem.txt')
# t=f.read()
# if 'twinkle' in t:
#     print('twinkle is present')
# else:
#     print('twinkle is not present')
# f.close()

# 2.
# def game():
#     return 64

# score=game()
# with open("hiscore.txt") as f:
#     hiscoreStr=f.read()

# if hiscoreStr=='' :
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))
 

# elif int(hiscoreStr)<score :
#     with open("hiscore.txt","w") as f:
#         f.write(str(score))


# 3.--file have been created

# # 4.

# with open("script.txt") as f:
#     content=f.read()

# content=content.replace("donkey","!@#$%^")

# with open("script.txt","w") as f:
#     f.write(content)

# 5.
# words=["donkey", "animal", "dog"]
# with open("script.txt") as f:
#     content=f.read()


# for word in words:
#         content=content.replace(word,"!@#$%^")
#         with open("script.txt","w") as f:
#             f.write(content)


# 6S
# with open("log.txt") as f:
#     content=f.read()

# if 'python' in content.lower():
#     print("yess python is present")
# else:
#     print("No python is not present")

# 7.
# content=True
# i=1
# with open("log.txt") as f:

#    while content:
   
#     content=f.readline()
 
#     if 'python' in content.lower():
#         print(content)
#         print(f"yess python is present on line number{i}")
#         print(i)
#     i+=1


# 8.
# with open("this.txt") as f:
#     content=f.read()
# with open("copy.txt","w") as f:
#     f.write(content)

# 9
# file1 ="copy.txt"
# file2="this.txt"

# with open(file1) as f:
#     f1=f.read()

# with open(file2) as f:
#     f2=f.read()

# if f1 == f2:
#     print("files are identical")
# else:
#     print("files are not identical")

# 10

# with open("this.txt","w") as f:
#     f.write("")

# 11.
# import os
# oldname="this.txt"
# newname="renames_by_python.txt"
# with open(oldname) as f:
#     content=f.read()

# with open(newname,"w") as f:
#     f.write(content)

# os.remove(oldname)