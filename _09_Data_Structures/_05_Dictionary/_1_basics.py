list1 = [1, 2, 3, 4, 5]
empids = [1, 2, 3, 4, 5]
e_names = []
# 100 employee data  {eid name sal age adreess} # [{},{},{},{}]

m_bill = [11.2, 124, 32, 213, 43]
e_data = [100, 'Madhu Nettem', 45000, 'Male', 'Bangalore', '560037', ['123', 'Marthahalli']]
# address
print("Employee data : ", e_data)

order_details = [12123321, 2133213, 12323, 'TLEE234e3', 43243, '43242']

# Immutable: int float bool string tuple
# Mutable  : list, dict, set
# json format
# UI ---> Python ---> Database

e_data = {'eid': 50000,
          'name': 'Madhu Nettem',
          'sal': 45000,
          'gender': 'Male',
          'eid': 123,
          'loc': 'Bangalore',
          'pin': '560037',
          'address': {'hno': '5456', 'area': 'Marthahalli', 'data': [12, 32, 13, 34]}
          }

'''
1. Dictionary keys must be UNIQUE
2. Dictionary keys must be IMMUTABLE
'''
print("Before : ", e_data)
print("Data  : ", e_data['loc'])
print("House no : ", e_data['address']['hno'])
print("House no : ", e_data['address']['data'][1])


'''
Map<String,Integer> map = new HashMap<String,Integer>()
map.add('eid',100)

di = {}
di = {'eid':100}

'''

mob_no = '324324324'  # int(input("Enter mobile no"))
e_data['mobile_no'] = mob_no  # will create new item
e_data['sal'] = 50000         # will update existing key sal
# create list.iterate through

print("After  : ", e_data)

print("Emp sal    :", e_data['eid'])
print("Emp area   : ", e_data['address']['area'])  # list[2][3]
print("Emp area   : ", e_data['address']['data'][2])


e_data = {'eid': 45000,
          'name': 'Madhu Nettem',
          'sal': 95000,
          'gender': 'Male',
          'eid': 123,
          'loc': 'Bangalore',
          'pin': '560037',
          'address': {'hno': '5456', 'area': 'Marthahalli', 'data': [12, 32, 13, 34]}
          }
print("Emp sal    :", e_data['eid'])



print("----------Dictionary items----------")
for key, val in e_data.items():  #  [('eid', 45000), ('name','Madhu Nettem')]
    print(key, "-----", val)

print("----------Dictionary keys----------")
for key in e_data.keys():  # ['eid','name','sal',....]
    print(key)

print("----------Dictionary values----------")
for val in e_data.values():  # [,,,,]
    print(val)




# UI ---> Python ----> Database
'''
Signup    
-----------
firstname : Madhu
lastname  : Nettem
mobileno  : 7406332332
mailid    : xyz@gmail.com
userid    : xyz
password  : xyz@13
gender    : Male
location  : Bangalore   
# json format *** 

# 100 signup users information  ==> list of dictionaries

user_info = [{'name':'madhu','pass':'123'}, {}, 2,3,4,5....100]

for user in user_info:
    user['pass'] = '456'

user_info = {'udata':[{'name':'madhu','pass':'123'},.......]
             }
'''
# ev_nos = [2,4,6,8,10....]
e_ids = [1, 2, 3, 4, 5, 6, 7]

order_details = [123213, 3432, 'Madhu Nettem', 'Bangalore', 543.56, 23, 5, '560037', 4]

order_details = {'order_no': 123213,
                 'ref_no': 3432,
                 'cust_name': 'Madhu Nettem',
                 'del_loc': 'Bangalore',
                 'total_bill': 543.56,
                 'discount': 23,
                 'disc_percnt': 5,
                 'pin_code': '560037',
                 'no_of_items': 4,
                 }

# order_details[5]
# order_details['discount']

print("Order details : ", order_details)
print("Location : ", order_details['del_loc'])
print("Order No : ", order_details['order_no'])
# print("Order No : ", order_details[100])


'''
Dictionary : 
    - Mutable data structure
    - Unordered
    - Key value pair i.e, item 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE and values can be anything
        
'''
# 1. Keys must be IMMUTABLE and values can be anything
dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'Madhu',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),
         [1, 2, 3]: {1: 1, 2: 2},  # Wrong, List is mutable
         {1: 1, 2: 2}: "Hello",   # Wrong, dict is mutable
         {1, 2, 3}: "Hello"     # Wrong, set is mutable
         }

print("Keys immutable : ", dict1)
# Dict keys should not be List, Dictionary, Set

# 2. Keys must be Unique
x = 10
x = 20

dict1 = {10: 100,
         20: 200,
         10: 150
         }

'''
hash table 
-------------
key    value
-------------
10     150
20     200
'''
list1 = [11, 22, 33]
print(list1)
print(list1[2])


print("Keys must be unique :", dict1)


