#Mohammed Anwar
Title = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@ Calculatr or whatever @@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

print(Title)

#----------------------------------------------

#OP 1 + , 2 - , 3 * , 4 /

OP = int(input("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Choose the type of opration:
1.Summation
2.subtracion
3.multiplcation
4.division
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""))

if OP == 1:
    x= int(input("the first number"))
    y= int(input("the seconed number"))
    z= x+y
    print("the sum of %d and %d is %d"% (x,y,z) )
if OP == 2:
    x= int(input("the first number"))
    y= int(input("the seconed number"))
    z= x-y
    print("the subtraction of %d and %d is %d"% (x,y,z) )
if OP == 3:
    x= int(input("the first number"))
    y= int(input("the seconed number"))
    z= x*y
    print("the multiplaction of %d and %d is %d"% (x,y,z) )
if OP == 4:
    x= int(input("the first number"))
    y= int(input("the seconed number"))
    z= x/y
    print("%d divided by %d equal %d"% (x,y,z) )
#----------------------------------------------------
