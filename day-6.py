#Day-6
'''
#assessment
#1.)python program to capitalize the first and last character of each word in a string
s1 = input("enter string")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[-1:len(s1)-1]+lst)

#2.)inpot = 128
#output = yes
#128 % 1 == 0,128 % 2 == 0,and 128% 8 ==0
n = 128
temp = n
f1 = 0
while n!=0:
    rem =n%10
    check = temp % rem
    if check!=0:
       f1 = 1
    n = n//10
if f1==0:
    print("yes")
       
else:
      print("no")

#3.)l1 = [1,2,3,4],l2 = [5,6 7,8] add both l1 and l2  ans=[6,8,10,12]
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3=[]
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)

#! ----->set

# charctristics of set
#1.)set can be created using{}
#2.)elements inside set are not indexed
#3.)does not allow duplicate values
#4.)it unordered
#5.)heterogenous --->acceot only unmutable datatypes
#6.)mutable or changable
#eg-1
s1 = {9,9,89,7.76,8+7j,(8,7,5),"TRUck",'e'}
print(s1)


#eg-2
s2 = {5,8,98,[9,0]}
print(s2)--->error


#eg-3
#min(),min(),len()

#ed-4
# to add elements inside set
s1 ={8,78,67,'u'}
# add()
s1.add(43)
print(s1)

#upadate()
s1.update([9,0])
print(s1)

# to delete aiement inside set
s1 = {8,78,67,'u'}

#pop()--->to delete one element randonly
s1.pop()
print(s1)
#remove()
s1.remove(78)
print(s1)


#discard()
s1 = {8,78,67,'u'}
s1.discard(67)
print(s1)
# remove
s1 = {8,78,67,'u'}
s1.remove(67)
print(s1)

#clear()
s1 = {8,78,67,'u'}
l1 = {}
print(type(11))
s1=set()
print(type(s1))

s1 = {8,9,0}
s1.clear()
print(s1)

#--->joint sets
s1 = {9,0,8}
s2 = {9.0,"card",'t',56}
#union()-->ombine 2 tests
s3 = s1.union(s2)
print(s3)
#intersection()
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))

s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))


#isdidjioit(),issubset(),issuperset()
s1 = {8,9,0}
s2 = {6,7,5,8,9,0}
print(s1.issubset(s2))
print(s2.issuperset(s1))

#--->problrm-1

s1 = {1,2,3,4,5,}
s2 = {3,2,7,8,9}

# n1 = {1,2,3}--->s1
for val in s1:
    if val in s2:
        str = "its joit set"
print(str)

#--->its a jointset
#--->dictionary
#eg-1
d1 = {1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
#7.)Key does nat allow mutable datatypes , Values allow mutable datatypes


d1 = {1:100,'a':200,4.5:"hello"}
#to access element in dictionary
print(d)
#or
#to access the values ,have to use key
print(d1[1])

#some common functions
#len(),max(),min()
print(min(d1.value()))
print(max(d1.values()))

#  Dictionary based functions
# To add element(key and value pair) in dict

d1 = {1:100, 2:200, 3:300, 4:400}
d1[5]=500
print(d1)

# To replace a value in dictionary
d1={1:100, 2:200, 3:300, 4:400}
d1[2]= "mango"
print(d1)

# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300,4:400}
#pop item()
d1.popitem()
print(d1)

#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple",

d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)


#pop()
#d1.pop(2) # ---> 2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 dictionary
#update()
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}
#delete element from dictionary

#d1 = {1:100, 2:200, 3:300, 4:400}
#popitem()
#d1.popitem()
#print(d1)


#pop
#d1.pop(2) #2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 ditionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple","b":"ball","c":"cat"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}
print(d1[90])
print(d1.get(90))

#to print all the keys
print(d1.keys())
print(d1.keys())

#to print all the vaules
print(d1.values())

#itertating dictionary
for val in d1:
    print(val)
for val in d1.values():
    print(val)
#to get both key and vaules
for key ,val in d1.items():
    print(key,val)


n=int(input("Enter of times:"))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("Enter of values:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) ==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
        
print(set3)

# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
#-->problem3
l1 = [1,2,3,4]
l2 = ["a","b","c","d"]
d1  = {}
d1[l1[0]]=l2[0]
d1[l1[1]]=l2[1]
d1[l1[2]]=l2[2]
d1[l1[3]]=l2[3]
print(d1)

'''

























