
# len()
e_data = {'eid': 45000,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',
          'office': 'Bangalore'
          }

print("Length of dict : ", len(e_data))

e_data['eid'] = 100


# type()
print("Length of dict : ", type(e_data))

# str()
di_str = str(e_data)
print("Dict in string format :", type(di_str), di_str)

# dict()
# di2 = dict({})


# Builtin functions:
#=======================
e_data = {'eid': 100,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',
          'office': 'Bangalore'
          }

print("-----------1. KEYS----------")

# 1. keys() :To retrieve all keys from dictionary
d_keys = e_data.keys()
print("E Data keys1 : ", d_keys, type(d_keys))
d_keys = list(e_data.keys())  # ['eid', 'name', 'sal', 'mobile', 'office']
print("E Data keys2 : ", d_keys, type(d_keys))

print("-----For loop ------")
for key in e_data.keys():   # list(e_data.keys())
    print(key)

print("-----------2. values()----------")
# values() : To retrieve all values from dictionary
d_vals = e_data.values()
print("E Data values1 :", d_vals, type(d_vals))
d_vals = list(d_vals)  # [100, 'MadhuN', 14000, '7406900500', 'Bangalore']
print("E Data values2 :", d_vals, type(d_vals))

print("-----For loop ------")
for val in e_data.values():  # list(e_data.values())
    print(val)


print("-----------3. items() ----------")
# 3. items() : To retrieve all items from dictionary
items = e_data.items()
print("E DATA Items : ", items, type(items))
items = list(items)  # [('eid', 100), ('name', 'MadhuN') .... ]
print("E DATA Items : ", items, type(items))




print("Iterating through dict items")
for item in e_data.items():
    print(item)

print("-------------------")
n1, n2 = (1, 2)  # tuple unpacking
print("Values : ", n1, n2)

for key, val in e_data.items():
    print(key, " --- ", val)


# 4. update()
print("-----------4. update() ----------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)

dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
dict1.update(dict2)
print("Dictionary Update  : ", dict1, dict2)

print("-----------5. clear() ----------")
di = {1: 1, 2: 2, 3: 3, 4: 4}
print("Before clear : ", di)
di.clear()
print("After clear : ", di)

print("-----------6. fromkeys() ----------")

di = {1: 1, 2: 2}
di = di.fromkeys([10, 20, 30, 40], "Hello")
print("Dictionary from keys : ", di)


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
list2 = list1.copy()  # list2 = list1
print("Shallow copy before at Index: ", list1, list2)
list2.append(100)
print("Shallow copy after at Index : ", list1, list2)

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

print("-----------8 . has_key() ----------")

dict1 = {1: 1, 2: 2, 'Hello': 'Madhu'}

print("Has key : ", dict1.has_key('Hello'))
print("Has key : ", dict1.has_key(1))
print("Has key : ", dict1.has_key(10))

'''
pop() popitem() setdefault()
'''

print("-----------8 . get() ** ----------")
# UI  --->   Python <--- Database

# ecommerce:
my_order = {'orderno': 12123232,
           'ref_no': 324324,
           'items_qty': 4,
           'price': 324324,
           'del_addr': []
            }
# if we know key exists in dictionary
print("Order price1 :", my_order['price'])
print("Order adddr1 :", my_order['address'])   # ERROR

# if we are not sure whether key exists in dict or not
print("Order price2 :", my_order.get('price'))
print("Order adddr2 :", my_order.get('address'))  # None

print("Order price3 :", my_order.get('price', 0))
print("Order adddr3 :", my_order.get('address', 'Bangalore'))  # Bangalore

# field validation
if my_order.get('pincode') == None:
    my_order['pincode'] = '560037'

print("--pin code---", my_order['pincode'])



# singup loginpage username password
e_data = {'eid': 43243,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',  # 91-7406900500
          'office': 'Bangalore'
          }
print("Employee data : ", e_data)
print("Employee name : ", e_data['name'])
print("Employee mobile  : ", e_data['mobile'])
# print("Employee name : ", e_data['company'])  # ERROR
print("Employee company : ", e_data.get('company'))  # to avoid exception
'''
if di.get('comp') == None: 
    di['comp'] = 'ORACLE'

'''
print("Employee company : ", e_data.get('company', 'ORACLE'))  # to set default value if key doesnot exists
print("Employee sal     : ", e_data.get('sal', 0))
print("Employee xyz     : ", e_data.get('xyz', 'XYZ'))

print("Employee name : ", e_data.get('name'))
print("Employee name : ", e_data.get('mobile'))
print("Employee name : ", e_data.get('mobile', '----------'))
print("Employee name : ", e_data.get('company'))
print("Employee name : ", e_data.get('company', 'ORACLE'))

'''Aadhar card info '''

aadhar_deatils = {'a_no': 32423423213123,
                  'name': 'Madhu Nettem',
                  'email': 'nettemmadhu@gmail.com',
                  'mobile': '7406900500',
                  'location': 'Bangalore'
                  }


aadhar_deatils = {'a_no': 32423423213123,
                  'name': 'Madhu Nettem',
                  'location': 'Bangalore'
                  }

'''
Database:
-----------------------------------------------------------------------------
SNo A_NO       NAME         MOBILE       EMAIL                    LOCATION 
-----------------------------------------------------------------------------
11   3243243   madhu       7406900500    nettemmadhu@gmail.com    Bangalore
12   3243244   ramu        2433242344          xyz@gmail.com      Bangalore
------------------------------------------------------------------------------
'''