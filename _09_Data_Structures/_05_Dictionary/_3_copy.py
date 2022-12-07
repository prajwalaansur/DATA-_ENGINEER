'''

'''
'''
Shallow Copy: copy()
            : Index Level : NO    RecursiveList: YES
Deep Copy   : deepcopy()
            : Index Level : NO    RecursiveList: NO
            


'''
print("-----------7. copy() ----------")
x = 10
y = x
list1 = [1, 2, 3]
list2 = list1
print("Before :", list1, list2)
print(id(list1), id(list2))
list2.append(10)
print("After :", list1, list2)

# list dict : It will not affect original content
           # Shallow copy : Recursive structure will affect
# list shallow copy

list1 = [1, 2, 3]
list2 = list1.copy()
print("Shallow copy before at Index: ", list1, list2)
print("Shallow copy before at Index: ", id(list1), id(list2))
list2.append(100)
print("Shallow copy after at Index : ", list1, list2)
print("-----------------------------")
list1 = [1, 2, [10, 20]]
list2 = list1.copy()
print("Shallow copy before at recursive: ", list1, list2)
list2[2].append(100)
print("Shallow copy after at recursive : ", list1, list2)

# list deep copy
import copy
list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)
print("Deep copy before at Index   : ", list1, list2)
list2.append(100)
print("Deep copy after at Index    : ", list1, list2)

list1 = [1, 2, [10, 20]]
list2 = copy.deepcopy(list1)
print("Deep copy before at recursive: ", list1, list2)
list2[2].append(100)
print("Deep copy after at recursive : ", list1, list2)

di1 = {1: 1, 2: 2}
di2 = di1.copy()
print("-----Before modification-----------")
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)
print("-----After modification-----------")
di2['name'] = 'Madhu'
print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)

