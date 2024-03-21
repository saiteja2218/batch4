#day-10

#) Tasks
# Write the code for the belwo tasks using function
# 1.) d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'
d1 == {"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
for val in d1:
      if d1 [val] = min(d1.values());
             print(val)
for val in d1:
      if d1 [val] = max(d1.values()):
              print(val)
for val in d1:
      if val.startswith('s') or val.startswith('S'):
          print(val)c

'''
# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6]
# n=2 --> [5, 6, 1,2,3,4]
# n=3--> [4,5,6, 1,2,3]
#eg-1
#method riding
#ploymorphism in classes using inheritance

class bank:
    def ratio(self):
        print("all banks has repo rate")
class SBI (bank):
    def ratio(self):
        print("SBI rate is 9%")
class IOB (bank):
    def ratio(self):
        print("IOB rate is 7.5%")
i = IOB()
i.ratio()
s = SBI()
s.ratio()

#eg-2
class USA:
    def langauge(self):
        print("english")
    def capital(self):
        print("washington DC")
class india(USA):
    def langauge(self):
        print("none")
    def capital(self):
        print("new delhi")
i = india()
i.langauge()
i.capital()

#eg-3
#polymorphism using objects
#c1,c2-->c1 = print(c1),print(c2)
#f1,f2
#eg-4
class c1:
    def f1(self):
        print("class 1")
class c2:
    def f1(self):
        print("class 2")
obj1 = c2()
obj2 = c1()
def display(a):
       a.f1()
display(obj1)
display(obj2)

#changing the functionality of builtin function
a = 9
b = 6
print(a.__add__(b))
class shopping:
    def __init__(self,l1):
        self.items = l1
    def __init__(self):
        length = len(self.items)
        return length
s = shooping([1,2,3,4,5])
print(len(s))

#--->method overloading
#eg-1
class suming:
    def  add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
s = suming()
#s.add(4,3)
s.add(4,5,1)


#eg-2
class summing:
    def add(self,a=none,b=none,c=none):
        if a!=none and b!=none and c!=none:
            print(a+b+c)
        elif a!=none and b!=none:
            print(a+b)
        else:
            print(a)
obj =summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)



# ! ----> Abstraction
# The process of hiding the implementation details is abstraction

# ? Eg_1:-

class shapes:
    def sides(self):
        print('All shapes have sides except circle')
class triangle:
    def triangle_sides(self):
        print("3 sides")
class square:
    def square(self):
        print("4 sides")
    def sides(self):
       pass
s = shapes()
s.sides()
tr = triangle()
tr.triangle_sides()
# ! Rules to define abstract class 1
#1.) Abstract class cannot be instantiated
#2.) From abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) Convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes

# ! Eg:2
# super() ---. used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")
    def m1(self):
        pass
class2 = c2()
class2.m2()



# * Eg_3:-
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sai2003"
        return pswd
class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name, '!!')
            print("Login Sucessful")
        else:
            print("Please check the password")
    def pwd(self):
        pass
Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)



#encapsulation
#eg-1
class car:
    name = "BMW" #private variable
    print(__name)
c1 = car()
print(c1.name)
c1.name = "audi"
print(c1.name)

#eg-2
#accessing private date outside the class
class c1:
         __phone = '7656567687'
         def display(self):
               print(self.__phone)
c = c1()
c.display()

#--->eg-3
#declare private method
class class1:
    def __m1(self):
        print("i am private method")
    def __init__(self):
        self.m1()
c = class1()
c.__m1()#error

#nested class
class class1:
    class class2:
          name = "sidhu"
          def display(self):
              print(self.name) 
    obj1 = class2()
obj = class1()
obj.obj1.display()

'''
























