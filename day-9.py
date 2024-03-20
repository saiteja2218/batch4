#day-9
'''
#ass-1
#2.)find the uncommon words from 2 strings
s1="Hello how are you"
s2="Hello how is"
s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)       
for val in s2:
    if val not in s1:
        print(val)
        
#3.)write a code print the 8th fibanocii number
#0,1,1,2,3,5,8
num = 8
n1 = -1
n2 = 1
for val in range(num):
    ans = n1+n2
    print(ans)
    n1 = n2
    n2 = ans
# constructors

#eg-2
#unparametarised constructor
class profile:
    def __init__ (self):
         print("hello world")
obj =profile()
obj.__init__()

#eg-3
#parameterised constructor
class profile:
      def __init__(self,id,name,age):
          print(id,name,age)
obj = print(1,"sai",21)

#eg-4
class c1:
    email = "sai"
    def m1(self):
        name = "teja"
        age = 21
        return name,age
    def display(self):
        #print(name,age)
        #print(self,name,self.age)
        print(self.m1())

object = c1()
object.display()

#eg-5
class class1:
    def __init__ (self):
        self.  name = "sai"
        self.email = "teja@gmail"
       #return name,email#error-->cannot use return with constuctor

    def display(self):
        print(self.name,self.email)
c1 = class1()
c1.display()

#----*inheritance

#eg-1
#the process of utilising the methods and attributes of parent class
#throught the object of child class it is called as inheritence

#5 types of inheritence

#single inheritence
#multilevel  inheritence
#multiple  inheritence
#hybid  inheritence
#heiraichal  inheritence

#---->single  inheritence
#it has only one parent class and only one child class

#eg-1
class parent:
    def m1(self):
        print("i am parent class")

class child(parent):
    def m2(self):
        print("i am child class")
obj = child()
obj.m1()

#eg-2
class c1:
    def __init__(self):
        print("i am constructor from parent class")
class child1(c1):
    pass
obj = child1()

#eg-3
class parent:
    name = "sidhu"
class child (parent):
    name = "name1"
    def display(self):
        print(self.name)
d = child()
d.display()


# ! Multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

# ! EXAMPLE:2
class honda_city:
    def honda_city_engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class amaze(honda_city):
    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def amaze_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class civic(amaze):
    def civic_engine_spees(self, cc, Hp, torque, fuel_type,num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def civic_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class Honda(civic):
    pass
honda = Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

# * Multiple Inheritance
# ? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")
class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)


 #! Heirarical inheritance
class catagory:
    def weight(self,weight):
        print("weight")
    def display(self,color,taste):
        print(color,taste)
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste= "neutral taste"
        self.display(color,taste)
class carrot(catagory):
    def carrot_specs (self):
        color="green"
        taste= "sweet"
        self.display(color,taste)

#hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2:
    def m2(self):
        print("class2")
class c3:
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5:
    def m5(self):
        print("Class 5")
class c6:
    def m6(self):
        print("Class 6")
'''
#! -------> Polymorphism
# poly - many, morph--> form
# A function which has the ability t perform more than 1 functionality
# then it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

#pioymorphism in operators
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

print(6*7)
l1 = {1,2,3,4,5,6}
print(*l1)
#def f1(*args)
l1 = [1,2,3,4]
print(l1*0)





















