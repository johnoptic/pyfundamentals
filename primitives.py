# Primitive Data Types
#---------------------
x = 10.32
print(type(x))

y = 10
print(type(y))

z = "This is a string"
print(type(z))

b = True
print(type(b))

# isinstance function
#--------------------
print(isinstance(4.5,float))
print(isinstance(3.5,int))


# converting data types to float
#-------------------------------
number = 10
print(float(number))

anotherNumber = "33"
print(float(anotherNumber))


# Changing a variables string value
#----------------------------------
string1 = "Hello World"
string2 = string1
print(string1)
print(string2)

string1 = "I have now changed"
print(string1)
string2 = string1
print(string2)

# Changing the case in a string
#------------------------------
firstName = "john"
lastName = "mcewan"

print (firstName.title() + " - This is using the title method")
print(firstName.upper() + " - This is using the upper method")
print(firstName.lower() + " - This is using the lower method")

fullName = firstName + " " + lastName
print(fullName)
print(fullName.title())

# Concatenating different types
#------------------------------
# python can only concatenate the same data types. If you have different data types that you are trying to concatenate together. You must convert them to the same types. 

age = 34
print(type(age))

print(fullName.title() + " is " + str(age) + " years old.")

# Strip Methods
#--------------

myString = "   the quick brown fox jumped over the lazy dog   "

print(myString.strip()) # Strips whitespace from both ends
print(myString.lstrip()) # Strips whitespace from left end
print(myString.rstrip()) # Strips whitespace from right side

# More on Booleans
#-----------------

myBoolean = 10 > 20
print(myBoolean)

# Practise Time
#--------------
print("-------------")
print("Practise Time")
print("-------------")

myInteger = 15
print(type(myInteger))

myFloat = 6.36272
print (type(myFloat))

myBool = 5 < 10
print(myBool)

x = "Hello "
y = "World"
z = ", this is dog!"

print(x + y + z)



