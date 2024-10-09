# Working with Operators
#-----------------------
print("\n---------------------------------Arithmetic Operators------------------------------------")
# Arithmetic Operators

x = 4
y = 12
z = 3

print(x + z) # Addition
print(y - z) # Subtraction
print(x * z) # Multiplication
print(y/x)   # Division
print(x*x)   # 16 Squaring a variable
print(x**x)  # Exponential


print("\n---------------------------------Assignment Operators------------------------------------")
# Assignment Operators
a = 3 
print(a)

# ADD AND
a += 5 # a = a + 5  | The answer should be 8 
print(a)

# SUBTRACT AND
a -= 2 # a = a - 2  | The answer should be 6 
print(a)

# MULTIPLY AND
a *= 4 # a = a * 4\ | The answer should be 24 
print(a)

# DIVISION AND
a /= 3 # a = a / 3  | The answer should be 8 
print(a)

# EXPONENT AND
a **= 3 # a = a**3  | The answer should be 512 
print(a)

print("\n-------------------------------Comparison Operators--------------------------------------")
# Comparison Operators

# checking for Equality
b = 3
a = b
print(a==b) # returns a Boolean value of True because both are equal.

# checking for Not Equal
print(a!=b) # returns a Boolean value. Returns the value of False because the variables are equal . 

# greater than
a = 2
b = 4
c = 6
print(a > c) # returns a Boolean value of False because a IS NOT greater than c

# less than
print(a < c) # returns a Boolean value of True because a IS less than c

x = 22
y = 22
z = 33

# greater than or equals to
print(x>=y) # Should return a True value because they are equal
print(x>=z) # Will return a value of False because x is less than z


# less than or equals to
print(x<=y) # Should return a True value because they are equal
print(x<=z) # Will also return a value of True because x is less than z

print("\n-------------------------------Logical Operators--------------------------------------")
# Logical Operators

# and | returns a value of True if both statements are true
# or | returns a value of True if either statements are true
# not | reverse the state of the operand

a = 4

print(a >2 and a<7) # True
print(a> 2 and a<4) # False

print(a > 5 or a<3) # Returns a value false because both conditions are false
print(a > 5 or a<6) # Returns a True because one of the statements is true.

print(not(a > 2 and a < 7)) # both conditions are true but the NOT operator changes the values to False.
print(not(a > 2 and a < 4)) # True

print("\n-------------------------------Identity Operators --------------------------------------")
# Identity Operators are used to compare the objects, not if they are equal but actually the same object
print(a is b)
print(a is not b)

print("\n-------------------------------Membership Operators --------------------------------------") 
# Membership Operators
#in
numbers = ["1","2","3"]
print ("2" in numbers) # True

numberInts = [1,2,3,4,5]
print(2 in numbers) # False - Returns false value because numbers is a list of "strings" Wrong Variable!

#not in
print(not("This is not in numbers!" in numbers ))
print(3 not in numberInts)

print("\n-------------------------------BitWise Operators --------------------------------------") 
# Bitwise Operators
# bin function
a = 444
b = 27031989
print(bin(a))
print(bin(b))
print(bin(64))
print(bin(130))

# & AND shares values in both variables binary sequences
a = 24
b = 60
print(a & b)

x = 223
y = 111
print(x & y)

# | OR in either binary sequence
a = 24
b = 60
print(a|b)

x = 223
y = 111

print(x|y)

# ^ XOR (set to 1 if only one is 1) can only be in one or the other of the binary sequences of the variables.
a = 24
b = 60
print(a ^ b)

x = 223
y = 111
print(x^y)

print("\n-----------------------------------Operator Precidence-----------------------------------")
# PEMDAS
# Order of Precidence
# Parenthesis ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

a = 3
b = 9
c = 4

print(b/a + c) # 7
print(b**a/c)
print(a + b * c)
print(a * a+c)
print(a/b * c)
print(a-b + c)
print(a**c*b+c*a/a)