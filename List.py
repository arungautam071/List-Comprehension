num =[1,2,3,4,5,6,7,8,9,10,11]

#long method
#-----------------------------------------------------------------------------

my_list=[]
for n in num:
    my_list.append(n)
print(my_list)

#-----------------------------------------------------------------------------

#By using list Comprehension

#------------------------------------------------------------------------------
my_list = [n for n in num]
print(my_list)


#------------------------------------------------------------------------------
my_list1 =[]
for n in num:
    my_list1.append(n*n)
print(my_list1)   

#------------------------------------------------------------------------------


my_list1=[n*n  for n in num]
print(my_list1)

#------------------------------------------------------------------------------

#Using Lamda AND Map

my_list1= list(map(lambda n: n*n, num))
print(my_list1)

#------------------------------------------------------------------------------

# I want "n" for each "n" in nums if "n" is even

my_list1=[]
for n in num:
    if n%2 == 0:
        my_list1.append(n)
print(my_list1)      

#------------------------------------------------------------------------------

my_list1=[n for n in num if n%2==0]
print("this is list 1")
print(my_list1)

#------------------------------------------------------------------------------

#i want a (letter,num) pair for each letter in "abcd" and each number by "0123"
my_num_list=[]
for n in "abcd":
    for i in range(4):
        my_num_list.append((n,i))
print(my_num_list)        

#------------------------------------------------------------------------------

my_list=[(Letter, Number) for Letter in "abcd"  for Number in range(4)]
print(my_list)

#------------------------------------------------------------------------------

names=['Bruce','Clark','Peter','Logan','Wade']
hero=['Batman','Superman','Spiderman','Wolverine','Deadpool']
my_dict={}
for i,j in zip(names,hero):
    my_dict[i]=j
print(my_dict) 

#------------------------------------------------------------------------------

my_dict={names: hero for name, heros in  zip(names,hero)}
print(my_dict)