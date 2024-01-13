# ''
# ""
# ''' '''
# concate:a+b
# slicing : g[0] or range[0:2]
#h[0]="a" --> does not work
# h[:4] is same as h[0:4]
# slicing with skip value: [1:6:2]
# string function
# 1.len()
# 2. a.endswith("v")
# 3.a.count("a")
# 4.a.captalize
# 5.a.find("hritik")
# 6. a= a.replace("a","b")
# escape sequence
# \n :iske baad sab new line pe 
# \t :Tab 
# \' : single quote
# \\ : backslash


# practice
# 1.
# x=input("enter your name\n:")
# print('good morning, '+ x )


# 2.
# letter=''' Dear <|Name|>
# you are selected!

# Date: <|Date|>
# '''
# name=input("enter the name\n")
# date=input("enter the date\n")
# letter=letter.replace("<|Name|>", name)    #remember store replace in one variable then obly replace is apply
# letter=letter.replace("<|Date|>", date)
# print(letter)

#3.
# st= "This is a string with double   spaces"
# doublespace=st.find("  ")
# print(doublespace)

#4
# st= "This is a string with double   spaces"
# st=st.replace("  ","")
# print(st)

# # #5
# letter="Dear Harry,This Pyton course is nice. Thanks!"
# print(letter)

# format_letter="Dear Harry,\n\tThis Pyton course is nice!\n Thanks!"
# print(format_letter)