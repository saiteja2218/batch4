#Day_2
# ---->swapping of variables
#Eg-1
a=7
b=5
#print(a,b)
temp = a
a = b
b = temp
#print(a,b)

a, b = b, a
#print("a =", a)
#print("a =", a)
#print(a,b)

a = a + b
b = a - b
a = a - b
#print(a,b)

a = a * b
b = a / b

a = a / b
#print(a,b)

# id()---> used to find the memory address of the variable
a = 7
b = 9
#print(id(a))
#print(id(b))

#----->keywords
#keywords are reserved words which provides special meaning to
#compiler or interpretor

import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))

#to check if the string is  keyword or not
#print(keyword.iskeyword("sai"))#flase

# ---->  literals
#literal is the constant value assigned to a variable
#A variable is considers to be constant whwn it  ois defines
#in caps
a=78# variable
A=78#consant

#hash() ---->it creates a hash value for constant datatypes and provides error for non constant datatypes
n1 = 89+7j
#print(hash(n1))

f1 = [7,8,9]
#print(hash(f1)) #error --->list is non-constant or mutable datatype
#print(hash(f1))
a=9
b=9
b=90
#print(id(a)) #print(id(b))

# ! ---> operators
# operators are symbols which is used to perform various operations between 2 or more operands
# arithmatic
# assignment
# logical
# relational or comparision
# bitwise
# identity
# membership

# to do ---> arithmatic --> =,-,*,?,%,//,**
#EX:1
a=8
b=6
c=9
#print(a+b+c)

# input() ---> used to get the runtime input
#n1=input("enter the value")
#print(n1)

#input() ----> used to get runtime values of all datatypes
#n1=eval(input("enter the value"))
#print(type(n1))

a=4
b=2
#print(a/2)# is used to get the quotient value
#print(a%b)#is used to get the reminder value

# --->float division

a= 765433
b = 19
#print(a//b)# ->the output will be inn integer & output will be based onfloor value

# --->assignment
a=5
a+=2
#print(a)
a= 30
a-=5
#print(a)

# ---> bitwise
a=7
b=4
#print(a&b)


# ----> logical
#and,or,not
a = 6
#print(a>3 and a<10)
#print(a>7 or a<30)
#print(not(a>8 and a<10))

# --->identity
#is,is not
a = 8
b = 8
#print(a is b)
# print(a==b)

a = (1,2,3)
b = (1,2,3)
#print(a is b)

a = [1,2,3]
b = [1,2,3]
#print(a is not b)

# ---> membership
num = 55
#print(num is 11)
#print(num is not 11)
num = 678
#print(8 is num)

# --> conditional statements
#if,elif,else

#eg-1
#if condition:
#    statement
#    statement
#    statement
#statement
#eg-1
a = 6
if a:
    print("hello")

#eg-2
a = 6
#if a>3:
#    print("yes")
#else:
#    print("no")
#eg-3
#if 7>8:
#    print("hello")
#print("no")

#eg-4
a = 0
a = None
a = False
a = ""
#if a:
#    print("yes")
#else:
#    print("no")
#a number is even or odd

#num = int(input("Enter a number: "))
#if (num % 2) == 0:
#   print(num,"is even")
#else:
#   print(num,"is odd")
# name,age,indian
#18 above,indian
name=int(int("sai"))
age=int(int("18"))
nationality=(int("indian"))
if age>=18:
    print("eligiable")
else:
    print("not eligiable")
        

   






