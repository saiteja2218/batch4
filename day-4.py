#Day-4
# ---> while loop
#break using while loop
'''
# 1.) iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i == 27:
        break
    print(i)                                
    i+=1

#2.)
i = 20
while i<31:
     print(i)
     i+=1

     if i == 27:
         break

#3.)
i = 20
while i<31:
     print(i)
     
     if i == 27:
         break
     i+=1

i = 20
while i<31:
    print(i)
    if i == 27:
         break
    i+=1
'''
'''
# ----> continue
#1.)
i = 20
while i<31:
    if i == 27:
        print(i)                                
    i=i+1
    continue

#2.)
i = 20
while i<31:
    i=i+1
    if i == 27:
        continue
    print(i)

#eg-5
#while to iterate from 12 to 22
i = 12
while i<23:
   print(i)
   i+=1

#find the sum of all numbers
i = 12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)

#find the average of value from 20 to 25
i = 20
sum=0
while i<26:
    sum=sum+i
    avg=sum/6
    i+=1
print(avg)
'''
'''
# --->nested for loop
#eg-1
for row  in range (1,3+1):
    for col in range(1,4+1):
         print(row,col)


row = int(input("enter the row:"))
col = int(input("enter the col:"))

for row in range (4):
    for col in range(4):
         print("*",end=" ")
    print()
   

sum=0
for row in range (5):
    for col in range(5):
        sum = sum+1
    print(sum,end=" ")
    print()

# to print stars in right angle triangle
for row in range (0,6):
    for col in range(0,row ):
         print("*",end=" ")
    print()

row = int(input("enter the row:"))
col = int(input("enter the col:"))

for row in range (row):
    for col in range(col):
         print("*",end=" ")
    print()


for row in range (0,6):
    for col in range(row,6 ):
         print("*",end=" ")
    print()


for row in range (6):
    for col in range(0,row ):
         print("*",end=" ")
    print()

# hollow square pattern

for row in range(5):
    for col in range(5):
        if row == 0 or row == 5 - 1 or col == 0 or col == 5 - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#triangle
for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# right angle triangle
for row in range(1, 5+1):
    for col in range(row):
        
        if col == 0 or col == row-1:
            print('*', end=' ')
        
        else:
            if row != 5:
                print(' ', end=' ')
                
            else:
                print('*', end=' ')
    print()
'''
# ---> list
#data types

#primary
#number-int,float,complex
#string
#booleaqn
#none

#collection
#list
#tuple
#set
#dictionary

# ---> list
#1.)if collection of elements are sorounded by square brackets,it is considered to be list
#
#eg-1
#l1=[4,7,9,9.89,"hello",7+9j,[8,9,0]]
#charactristics of list
#1.)list have to be sorrounded br[]
#2.)it is mutable(the elements in the list are changable)
#3.)every elements inside list is indexed
#4.)the elements inside list will be ordered format
#5.)it can hold dupilicate values
#6.)its haterogenous
#to access the elements in list
#lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#print(l1)

# --->indexing
#in collection datatypes like list,tuple,string,the elements will aloted
#with pre-defined unique value called index value
#we have 2 types of indexding
#positive indexing-->starts with 0 from left hand side
#negative indexing-->starts with -1 from right hand side
'''
#----->positive indexing
lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[0])
print(lst1[4])
print(lst1[20])#->error

lst1 = [1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-1])
print(lst1[-5])
'''
# -->slicing
#lst1 = [1,4,1,7,89.7,7.5,"p","i"]
#lst1[start_index:end_index:step]
#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[:8])
#print(lst1[3:])
#print(lst1[:])
#print(lst1[0:7:2])
#trail = int(input())
#print(lst1[-1:-4])
#print(lst1[-4:-1])
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

#to insert the add element inside list
#append()
l1 = [9,8,0,9]
l1.append("car")
print(l1)


    
