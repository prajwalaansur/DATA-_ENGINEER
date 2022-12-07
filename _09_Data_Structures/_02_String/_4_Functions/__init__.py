
#BUILT IN STRING METHODS
print("---Capitalize -- ", msg.capitalize()) # Capitalizes first letter of string
print("---Count-------- ",message2.count('O'),"  ",message2.count('O',6,15)) #start,end are optional

#String Formatting Operators
print("My name is %s and weight is %d kg!" % ('Zara', 21))

#ASCII  Unicode
str1 = "Madhu"
str2 = u"Madhu"
print(str1,"  ",len(str1),"  ",len(str2))
print(getsizeof(str1)," ",getsizeof(str2))
