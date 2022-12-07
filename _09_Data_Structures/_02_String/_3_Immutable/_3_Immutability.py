x = 10
print("Value : ", x, id(x))
x = 20
print("Value : ", x, id(x))

print("----------------------")


'''Immutable'''
'''
 CD RW-CD   DVD - RW-DVD
Harddisk : D Drive 50GB - existing - new memory - 1GB - new content
Pendrive : 5GB capacity 5GB - can't overwrite 
CD       : 700MB - one time 
RW-CD    : 700MB - rewrite data 
'''
'''
Immutable: Once a data type/data structure is created ,use it AS IS or delete it.
           We can't modify(update) the value at the given memory location.
-----------
Numbers : int float 
Boolean : bool
String 
Tuple 

Mutable : 
---------
List Dictionary Set
'''
msg = 'Hello'
print("Before : ", msg)
msg = msg + ' Welcome'
print("After : ", msg)







x = 10
print("First  :", x)
x = 20
print("Second :", x)
print("-----------------")
x = 10
print(x)
x = x + 10
print(x)
print("------------------")
msg = 'Hello'
print("Message : ", msg)
msg = 'World'
print("Message : ", msg)
print("------------------")
msg = 'Hello'
print("Message : ", msg)
msg = msg + 'World'
print("Message : ", msg)

print("--------------------------")
msg = 'Hello World'
msg = msg.replace('H', 'j')  # jello World
print(msg)
