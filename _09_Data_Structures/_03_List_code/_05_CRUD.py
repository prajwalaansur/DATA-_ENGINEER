# CRUD Operations


# 1. CREATE
list1 = [1, 2, 3, 4, 5, 6]

list1 = [1, 2, [30, 40, 50], (11, 22, 33), {1, 2, 3}, {1: 100, 2: 200}]

# 2. RETRIEVE
print('List values1 : ', list1)
print('List values2 : ', list1[2])
print('List values21 : ', list1[2][1])

# 3. UPDATE
list1[1] = 200
print('List values2 : ', list1)

# 4. DELETE
del list1[2]
print('List values3 : ', list1)
del list1
#print('List values4 : ', list1)

a = list(input("Enter list : "))   # [1,2,3]
print(a)
print([int(x) for x in list("1234")])
st = '[1,2,3,4]'
li2 = []
for val in st:  # '1' '2' '3' '4'
    if val.isnumeric():
        val = int(val)
        li2.append(val)
print(li2)
print([x for x in list()])

li = list("1234")
print(li)  # ['1','2','3','4']
li[0] = li[1] = 5  # [5,5,'3','4']
print(li)