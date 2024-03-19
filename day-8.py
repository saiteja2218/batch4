#day-8
'''
#eg-3
def profile(name,age,place):
     txt = "my name is{}.i am {}year old.i am from{}."
     print(txt.format(name,age,place))
profile("sai",21,"kadapa")

#eg-4
#function with retrun staement

def f1():
    z = 8
f1()
print(z)#error --->cannot use outside the function

# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

def f1(a,b):
    c = a*b
    return c
print(f1(6,8))
obj = (f1(6,8))
obj1 = f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

def isPalindrome(s):
      return s == s[::-1]
s = "lol"
ans = isPalindrome(s)
if ans:
   print("Yes")
else:
   print("No")
   
#problem-1

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a = int(input("enter the value:"))
palindrome(a)


#based on the declaration of parameter and args
#functions are divided into 5 catagories

#positional args
#keyword args
#default args
# variable lenght args
#keyword variable length args

#positional args
#the position of parameter a have to be same as position os arguments


#eg-1
def profile(name,phone,mark):
    txt ="My name is{}.My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))

profile(8044664522,"sai",97)

#keyword args
#to overcome the disadvantage of position args,we use keyword args
#it is the process of initialising the parameter with the args while calling the function
def profile(name,phone,mark):
    txt ="My name is{}.My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))

profile(phone=8074884522,name="sai",mark=95)

# todo ---> Exception of  keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))
#profile(name="savithri", 5672389021 ,mark=95) # error ---> positional args follow keyword arg
#profile(5672389021, name="savithri", mark=95) # error ---> names has multiple values
profile("savithri", mark=95, phone=5672389021)

# * Default args
# ? the method of assigning the argument to the parameter while declaring the function


# ! EXAMPLE :1
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
         txt="My name is {}. My phone number {}. I am from {} ."
         print(txt.format(name,phone,place))
    else:
         print("You are not eligible to Signup")
profile("Savithri",9876543210)

# * variable length params


# ! EXAMPLE:1
# ? To pass more then 1 arg to a parameter means we use variable length args
# To convert parameter to variable length param, add * to their prefix of parameter

#name="savithri", "pavithra ", 'name3'
def profile(*name):
    for val in name:
        print(" My name is",val)
profile("savithri", 'pavithra', 'name3')


# ! EXAMPLE:2
def profile(*name, age):
    for val in name:
        print("My name is",val, "may age is", age)
#profile("savithri", 'name2', 'name3', 20) # error ---> age has no args
def profile(age, *name):
    for val in name:
        print("My name is",val, "may age is", age)
profile(20, "sai",'name2', 'name3')


# keyword variable length args
#kwargs---->which is used to provide the args in the from of key value pair.

#eg-1
def price(**price_list):
    print(price_list)
price(shirt=1000,iphone=80000)


n=5
{1:1,2:4,3:9,4:16,5:25}
n=int(input("enter the number"))
d1={}
for val in range(1,n+1):
      d1[val]=val**2
print(d1)


def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val] = val**2
    print(d1)
dict1(5)



# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

#eg-1
class c1:
    name1 = "sai"
    print(name1)


    
#eg-2
class person:
    name = "sai"
c = person()# c os object
#the process of creation of an object is called as instantiation
print(c.name)


#eg-3
#create of a method
#when the function is created with a class is called as method

class person:
    def display(person):
        print("hello welcome to classes")
p = person()
p.display()



#eg-4
#method with parameter
class person:
    def display(person):
     print("hello welcome to classes")
p.person()
p.display("sai",21)


#eg-5
class person1:
    fname = "SAI"
    lname = "k"
    def first_name(self):
        print(self.fname)

    def full_name(self):
        print(self . fname+"  "+self . lname)
p = person1()
p .first_name()
p.full_name()
'''

#eg-6
#constructors--->_init_()
#this is a special method which has the ability to execute iotself without
#calling it manullay through the process of instantitaion
class profile:
#def_init_(self):# constructor method
        print("hey")
p = profile()

























