#Day-3

#eg-3
#take values of length and breadth of a
#from user and check if it is square or not.
#a=int(input("enter the length "))

#b=int(input("enter the breadth "))

#if a==b:

#  print(" is a square")

#else:

#  print("is not a square")
'''
#eg-4
#python program to check whether the
#given intger is a multiple of both 5 and 7
#number = int(input("Enter an integer: "))
#if((number%5==0)and(number%7==0)):
#    print( "is a multiple of both 5 and 7")
#else:
#    print( "is not a multiple of both 5 and 7")
'''
"""
#eg-5
#write a program to accept the cost price of a bike and display the
#road tax to be paid
#according to the following criteria:
#cost price(in Rs)                 tax
#>100000                            15% + discount 6%
#<100000                            5%
cp = int(input("Enter the cost price of the bike: "))
total = 0
if cp > 100000:
    discount = cp*(6/100)
    value = cp-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax = cp*(5/100)
    total = cp+tax
print("the on road cost of bike is:",total)
"""
'''
# ---> if elif else
#eg-1
a = 7
b = 9
c = 30
if a>b and a>c:
    print("Ais greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
'''
"""
#a school has following rules for grading system:
#a.below 25 -f
#b.25 to 45-e
#c.45 to 50-d
#d.50 to 60-c
#e.60 to 80-b
#f.above 80-a
#ask useer to enter marks and print the corresponding grade.

marks = int(input("Enter marks:"))
if marks<25:
  print ("F")
elif marks>=25 and marks<45:
  print ("E")
elif marks>=45 and marks<50:
  print ("D")
elif marks>=50 and marks<60:
  print ("C")
elif marks>=60 and marks<80:
  print ("B")
else:
  print ("A")
"""
#eg-6
#accept the age of people and display the oldest one.

'''    
# ---->short hand if else
#eg-1
a = 9
b = 6
if a>b:
    print("A")
else:
   print("B")

# --> using short hand if else
#rules
# 1.)statement inside the if condition have to be present at first
# 2.)elif can't be used in short hand if else
# 3.)always it have to end with else
a = 9
b = 6
print("A") if a>b else print("B")
'''
'''
# check vowels or consonent
char = input("enter the char")
if char=="a" or char =='e' or char =='i' or char =='o' or char =='u':
    print("is a vowel")
else:
    print("its consonent")

# or
str1 = "aeiouAEIOU"
if char in str1:
    print("vowel"
          )
else:
    print("consonent")

# shorthand if else
char = input("enter the char:")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print ("consonent")

'''
'''
# --->elif ladder using shorthand if else
#eg-1
#find greater among 3 variables using shorthand if else
a = 8
b = 5
c = 9
print("A is greater ") if a>b and a>c else print("B is greater") if b>a and b>c else print("C is greater")
'''
'''
#----> looping
#looping can be implimented using
#for loop
#while loop
# ---> for loop
#for loop is used for iteartion ,if we know the number of times the loop have to run
#it is used to iterate the iterables eg(string,list,tuole,etc...)

# todo ---->syntax for loop

for syntax in c
for(i=0;i<10;i++){
    print("hello")
}

#for syntax in python
# for userdefined_variable in range(start,end,step):default setp value is 1
#statement
#statement
#statement

#eg-1
# to print the value from 1 to 10 using for loop
for i in range (0,10):
    print(i)
    print("hello")
    print("sai")
'''
'''
#eg-2
for val in range(23,50,2):
     print(val)
for val in range(1,15,4):
     print(val)

#eg-3
#to decrement the value
for val in range(10,0,-1):
    print(val)
for val in range(10,0,-2):
    print(val)
for val in range(10,0,1):
    print(val)
    
#eg-4
#print the output of 7th multiplication table from 21 to 43
#num = int(input("Display multiplication table of? "))
for val in range(3,10-3):#(method-1)
   print('7','x',val,'=',val*7)
for val in range(3,10-3):#(method-2)  
    ans="7 x {} ={}"
    print(ans.format(val,val*7))
for val in range(3,10-3):#(method-3)
    print(f"7 x {val}={val*7}")

#eg-5
#break --> used to teerminate the loop
for val in range(1,10):
    print(val)
    if val == 6:
        break
#eg-6       
for val in range(1,10):
    if val == 6:
        break
    print(val)
#eg-7 
for val in range(1,10):
    if val == 6:
         print(val)
         break
'''
'''
# continue
#eg-1
for val in range(1,10):
    if val == 6:
        continue
    print(val)
for val in range (1,30):
    if val ==6 or val ==8 or val ==21:
        continue
    print(val)
#practise problems
#print the even number between 20 to 40
for val in range(20,41):
    if val %2==0:
        print(val)
'''

# ----> whilw loop
#while is used when we do not know the number of time the loop have be run
#to iterate the non iterable elements while loop is used

#todo syntax
#instialisation
#while condition:
#statement
#to iterate number from 1 to 10

i = 0
while i<11:
    print(i)
    i+=1 OR I+=1
#for loop practisee
#write a program to display sum of odd numbers and even
#numbers that fall between
#12 and 37 (including both numbers)
    









    
