print(10)
100
print(20)

str1 = 'hello'
print("Before : ", str1)
str1.capitalize()  # "Hello"
print("After  : ", str1)
print("After  : ", str1.capitalize())
str2 = str1.capitalize()
print("After  : ", str1, str2)
str1 = str1.capitalize()
print("After  : ", str1)
