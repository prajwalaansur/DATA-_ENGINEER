# list is mutable
# tuple is immutable


# CREATE
list1 = [1, 2, 3, 4, 5, 6, 5, 5, 6]
## RETRIEVE
# entire list
# part of list
# index


##UPDATE
# add elements at last
# insert elements
# add element in 0th index

# DELETE
## delete entire list
# delete part of list
# delete single value index/value

'''
# Builtin functions:
---------------------
append insert extend   : UPDATE
pop  remove            : DELETE 
count                  : RETRIEVE
index                  : RETRIEVE
reverse                : UPDATE 
sort                   : UPDATE
copy                   : CREATE
'''
# 1. append(): It appends element(any value) at end of the list
             # list1.append(obj) Appends any object obj to list
list1 = [1, 2, 3, 4, 5, 6]
print("Before append : ", list1)
list1.append(10)
print("After append  : ", list1)
list1.append([10, 20, 30])
print("After append  : ", list1)
list1.append(10.4)
list1.append(True)
list1.append('Hello')
list1.append([1, 2, 3])
list1.append((10, 20, 30))
list1.append({1: 1})
list1.append({100, 200, 300})

for ind, val in enumerate(list1):
    print(ind, "----", val)

print("After append  :", list1)

list1 = [1,2,3]
list1.append(5)
list1.append({1:1,2:2})
# list1.extend([])


list1 = [1, 2, 3]
print("Before list : ", list1)
list1.append([4, 5, 6])
print("After list : ", list1)



# extend  : only sequence str,list,tuple
         #: list1.extend(seq)         Appends the contents of seq to list

list1 = [1, 2, 3, 4, 5, 6]
# list1.extend(10)
list1.extend([1, 2, 3])
print("Before extend : ", list1)
# append([10,20,30]) :       ==> [1,2,3,4,5,6, [10,20,30]]
list1.extend([10, 20, 30])  #==> [1,2,3,4,5,6, 10, 20, 30]
print("After extend  : ", list1)
list1.extend('Hello World')
list1.extend((1, 2, 3))
print("After extend  : ", list1)


# append vs extend

list1 = [1, 2, 3]
list1.append([10, 20])    # [1, 2, 3, [10,20]]
list1.extend([100, 200])  # # [1, 2, 3, [10,20], 100, 200]
print("List after append,extend : ", list1)

# 3. pop # list.pop(obj=list[-1]) Removes and returns last object or obj from list
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before pop   : ", list1)
list1.pop(3)  # index
print("After  pop   : ", list1)  # [23, 12, 46, 14, 7, 2, 19, 25]
list1.pop()   # by default -1 index will be taken
print("After  pop   : ", list1)  # [23, 12, 46, 14, 7, 2, 19]

rem_ele = list1.pop(0)
print("Popped element : ", rem_ele)
print("After  pop   : ", list1)

# 4. remove
            # list.remove(obj)    Removes object obj from list
list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before removal1 : ", list1)
list1.remove(34)
print("After removal2  : ", list1)

list1 = [23, 14, 12, 46, 34, 14, 7, 2, 14, 19, 25]
print("Before removal3 : ", list1)
#list1.remove(14)
list1.pop(5)
print("After removal4  : ", list1)

# 5.list.insert(index, obj)  Inserts object obj into list at offset index
list1 = [1, 2, 3, 4, 5]
print("Before index : ", list1)
list1[0] = 150  # [150, 2, 3, 4, 5]  Replace the value in index
print("After index   : ", list1)
list1.insert(0, 150)  # [100, 150, 2, 3, 4, 5] Insert the value in index
print("After inse/rt  : ", list1)
list1.insert(3, 100)
print("After insert   : ", list1)

# 6. count ==> list.count(obj)Returns count of how many times obj occurs in list
list1 = [1, 1, 3, 2, 3, 2, 4, 5, 3, 2, 1]
print("List count 2: ", list1.count(2))

# 7. index  ==> list.index(obj) Returns the lowest index in list that obj appears
list1 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
print("List index : ", list1.index(53))
list1.insert(list1.index(53)+1, 1000)

li = []
for ind in range(len(list1)):
    if list1[ind] == 53:
      li.append(ind)
print("53 at : ", li)
counter = 0
for val in li:
    list1.pop(val+counter)
    counter -= 1


# 8. reverse ==> list.reverse()  Reverses objects of list in place
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print("List after reverse : ", list1)

# 9. sort ==> list.sort(obj)Sorts the elements
list1 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
list1.sort()  # ascending order   desc: reverse=True
print("List sort ascending : ", list1)

list1.sort(reverse=True)  # descending order
print("List sort descending: ", list1)

# 10. copy()


list1 = [1, 2, 3, 4, 5]
print("Before copy list1    : ", list1)
list2 = list1.copy()  # individual copy
print("After copy list2     : ", list2)
print("Normal copy function : ", id(list1), id(list2))
list1.append(100)

print("After append : list1 :", list1)
print("After append : list2 :", list2)

# 2nd way of copy

list1 = [1, 2, 3, 4, 5]
list2 = list1
print("Variable  copy : ", id(list1), id(list2))
list1.append(100)
print("After var copy :", list1, list2)
list2.extend([11, 22])
print("After var copy :", list1, list2)


list1 = [3, 1, 4, 5, 2]
list1.sort()
print("List sort: ", list1)


list1 = [3, 1, 4, 5, 2]
print("List sort: ", sorted(list1))
print("List sort: ", list1)


# Shallow Copy vs Deep copy