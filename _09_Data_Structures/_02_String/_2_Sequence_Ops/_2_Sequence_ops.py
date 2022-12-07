# String sequence operations

# SEQUENCE OPERATIONS
message = 'HELLO WORLD'
print("----------1. Indexing---------")
# 1. Indexing:
print("4th index : ", message[4])
print("5th index : ", message[5])
print("7th index : ", message[7])
print("9th index : ", message[9])
print("9th index : ", message[-2])
print("10th index : ", message[10])
print("10th index : ", message[-1])


print("----------2. Slicing---------")
# 2. Slicing : str[index:position]
message = 'HELLO-WORLD'
print("0 to 5 : ", message[0:5])  # 0th index to 5th position
print("2 to 5 : ", message[2:5])
print("3 to 7 : ", message[3:7])
print("3 to 7 : ", message[1:10])
print("-9 to 5 : ", message[-9:5])

print("----------3. Adding---------")
# 3. Adding :
str1 = 'Hello'
str2 = 'World'
print("Addition1 :", str2 + str1)
print("Addition2 :", str1 + ' ' + str2)


str1 = 'Hello '
str2 = 'World'
print("Addition3 :", str1 + str2)
print("Addition4 :", str2 + str1)


print("----------4. Multiplying---------")
# 4. Multiplying
str1 = 'HELLO '
print("Multiplication :", str1 * 5)

print("----------5. Membership ---------")
# 5. Checking for membership
print("H  : ", 'H' in 'HELLO-PYTHON')
print("L  : ", 'L' in 'HELLO-PYTHON')
print("LL  : ", 'LL' in 'HELLO-PYTHON')
print("PH  : ", 'P,H' in 'HELLO-PYTHON')
print("-  : ", '-' not in 'HELLO-PYTHON')
print("Space  : ", ' ' not in 'HELLO PYTHON')
print("B  : ", 'B' not in 'HELLO PYTHON')
message = 'HELLO-PYTHON'
print('H' in message)
print('L' in message)


str1 = 'Hello-World'  # Refer ASCII table  A-Z 65    a-z 97....

print("----------6. Length ---------")
# 6. len()
print("Length of string : ", len(str1))
#7. max()
print("----------7. Max ---------")
print("Max of string : ", max(str1))

#8. min()
print("----------8. Min ---------")
print("Min of string : ", min(str1))

'''
str1 = 'Hello World'

char = ''
String str1 = new String("Hello World")
StringBuffer
StringBuilder

emp_ids = [1,2,3,4,5,6,7] #list

List<Integer> list = new ArrayList<Integer>()
list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)
'''
message = 'HELLO WORLD'   # 0 1 2 3 4 5 6
print(message)

print("----String with for loop 1--------")
for char in message:
    print(char)

print("----String with for loop 2--------")
for char in message[0:5]:
    print(char)

print("----String with for loop 3--------")
for char in message[::-1]:
    print(char)

chars = ['P', 'H']
for char in chars:
    if char in 'HELLO PYTHON':
        print("TRUE")
