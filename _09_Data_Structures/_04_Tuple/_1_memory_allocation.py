x = 10  # write operation  CREATE
print(x)  # read operation  RETRIEVAL/READ
print(20)
print(10+20)
li1 = [1, 2, 3, 4]     # Mutable  Modifications
tup1 = (1, 2, 3, 4)    # Immutable No Modifications
print(tup1, type(tup1))


tup1 = ()
print("Empty tuple1 :", tup1, type(tup1))

tup1 = (1)
print("Empty tuple2 :", tup1, type(tup1))

tup1 = (1,)
print("Empty tuple :", tup1, type(tup1))


list1 = [1, 2, 3]
list2 = list1.copy()
print("Shallow Before   : ", list1, list2)
list2.append(100)
print("Shallow : After   : ", list1, list2)

list1 = [1, 2, 3, [10, 20]]
list2 = list1.copy()
print("Shallow Before   : ", list1, list2)
list2[3].append(100)
print("Shallow : After   : ", list1, list2)


from copy import deepcopy
list1 = [1,2,3]
list2 = deepcopy(list1)
print("Deep Before   : ", list1,list2)
list2.append(100)
print("Deep : After   : ", list1,list2)

list1 = [1,2,3,[10,20]]
list2 = deepcopy(list1)
print("Deep Before   : ", list1,list2)
list2[3].append(100)
print("Deep : After   : ", list1,list2)

'''
            Shallow Copy    Deep Copy
 Index         NO             NO 
 Recursive     YES            NO
'''




