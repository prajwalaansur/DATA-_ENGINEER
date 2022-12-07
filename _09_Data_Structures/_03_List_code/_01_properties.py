x = 10
'''
# REQ: so and so......
           1. CRUD     :  CREATE RETRIEVE UPDATE DELETE
           2. STATE    :  (Data types, Data structures)
           3. Behavior :  (Operators, DM, Loops)
'''
x = 10.5
is_bool = True
msg = 'Hello World'  # '@!#!@#3213213{}<>?<VCXVEWREWRSDFSDF'

list1 = [14, 12, 52, 33, 14, 25, 86]

print("List data structure :", list1)

'''List properties'''

'''
List properties:
==================
# 1. List is mutable
# 2. List allows duplicate elements
# 3. Maintains Insertion order
# 4. List will allow both homogeneous and heterogenous data
# 5. Follows indexing mechanism while storing elements(Sequence)
'''
# 1. List is mutable **
print("----List is MUTABLE-----")
list1 = [12, 22, 13, 54, 35]
      #  0   1    2   3   4
print("Before list : ", list1)
list1[2] = 300
print("After list1  : ", list1)
list1.insert(1, 100)
print("After list2  : ", list1)

# 1.List will allow both homogeneous and heterogenous data
    # Homo
print("----------Homogeneous---------")
list1 = [1, 2, 3, 4, 5, 6]
print('Integers is list : ', list1)

list1 = [1.5, 3.2, 5.6, 4.8]
print('Float is list   : ', list1)

list1 = [True, False, True, False]
print('Boolean is list : ', list1)

list1 = ['hello', ' world', 'welcome', 'python']
print('Strings is list : ', list1)
'''
| 1 2 3 
| 4 5 6   2X2
| 7 8 9



'''
'''
 [1, 2, 3]
 [4, 5, 6], 
 [7, 8, 9]   M[1][2]
 '''
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Lists   is list : ', list1)
print('Lists   is list : ', list1[0])
print('Lists   is list : ', list1[0][1])

list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print('Tuples  is list : ', list1)

list1 = [{1: 1, 2: 2}, {'id': 100, 'name': 'Madhu'}]
print('Dict    is list : ', list1)

list1 = [{1, 2, 3}, {4, 5, 6}]
print('Set is list : ', list1)

# Hetero
list1 = [100, 14.5, False, 'Hello', [1, 2, 3], (1, 2, 3), {1: 1, 2: 2}, {1, 2, 3}]
print("---Hetero-------", list1)

# 2. List allows duplicate elements
list1 = [10, 10, 20]
print("Duplicates in list : ", list1)

# 3. Maintains Insertion order
list1 = [1, 2, 3, 4, 5, 6]
print("Insertion order: ", list1)


# 5. Follow indexing mechanism
list1 = [12, 22, 13, 54, 35]
      #  0   1    2   3   4



'''
When to use list data structure:
---------------------------------
- Handle group of elements
- Homogeneous/heterogenous, 
- Mutable structures
- With Duplicate values 
'''
print("---------------------- LIST: SEQUENCE OPERATIONS ---------------------")
list1 = [1, 1.5, True, 'HelloWorld', 234]
       # 0   1    2       3           4
# Indexing
print("Indexing : ", list1)
print("Indexing : ", list1[1])
print("Indexing : ", list1[3], list1[-2])
print("Get o in list1 :", list1[3], list1[3][4])

# Slicing
print("Slicing : ", list1)
print("Slicing : ", list1[0:4])

# Adding
print("Adding 2 lists :", [1, 2, 3] + [4, 5, 6])
#Mulitiplying
print("Mulitply 2 lists :", [1, 2, 3] * 5)
# Membership
print("Check value : ", 1 in [1, 2, 3])
# len
print("Length of list1 : ", len(list1))

list1 = [1, 2, 3, 4, 5, 6, 7]
# max
print("MAX of list1 : ", max(list1))
# min
print("MIN of list1 : ", min(list1))


list1 = [1, 2, 3, 4, 5]
list2 = [True, False, False]
list3 = ['Hello', 'World', 'python']
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list4 = [(1, 2), (3, 4, 5)]
list5 = [{1: 1, 2: 2}, {1: 'Madhu', 2: 'Nethra'}, {}]
list6 = [{1, 2, 3}, {4, 5, 6}]

print("-----------List3 operations---------")
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("List3 : ", list3[0])
print("List3 : ", list3[0][1])
print("List3 : ", list3[0:1])
print("List3 : ", list3[1][2])
