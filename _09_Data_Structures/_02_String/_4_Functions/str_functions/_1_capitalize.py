100
'Hello World'

print(10)  # one time usage

x = 10
print("Value of x :", x)  # multiple usage


# 1. capitalize() :: Returns a string where the first character is upper case.

print("------------- 1. capitalize() -----------------")
print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello world'
print("Normal string           :", str1)
str1.capitalize()  # No action here  Hello World
print("String after capitalize :", str1)    # print(x)

print("String after capitalize :", str1.capitalize())   # print(10)
print("String after capitalize :", str1)    # print(x)
# str2 = str1.capitalize()                  # x = 10


'''3 Ways'''
print("----Way 1--------")
# 1 : Current string should be used as is, new string used "one time"
str1 = 'hello world'
print("String     : ", str1)
print("Capitalize : ", str1.capitalize())  # print(10)
print("String     : ", str1)

# 2 : Current string should be used as is, new string used in "multiple places"
print("----Way 2--------")
str1 = 'hello world'              # x = 10
print("String     : ", str1)
str2 = str1.capitalize()         #  y = x + 5
print("String     : ", str1)
print("String     : ", str2)     # print(x)

# 3 : Current string should get modified
x = 10
x = x + 20

print("----Way 3--------")
str1 = 'hello world'
print("String     : ", str1)
str1 = str1.capitalize()
print("String     : ", str1)

print("-------------------------------------------------------------------------------------")

# format   %s %d \n