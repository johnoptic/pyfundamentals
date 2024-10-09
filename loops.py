# if statements - conditional
x = 10
y = 20
z = 30

if x < y:
    print("x is less than y")
else: 
    print("x is not less than y")

x+=10
print(x)

if x < y:
    print("x is less than y") 
elif x == y:
    print("x and y are equal")
else:
    print("y is greater than x")

# for loops
colors = ["blue","red","green"]
for color in colors:
    print(color)

numbs = [0,1,2,3,4,5,6,7,8,9]
for number in numbs:
    print (number)
print("\n")

# range() function that determines how many times the loop will be repeated
for a in range(10): # creates a variable and prints up to 10
    print(a)
print("\n")
for b in range(10,35): # creates b variable and prints from 10 to 35
    print(b)
print("\n")
for c in range(0,100,2): # creates c variable and prints 0-100 incrementing every 2nd number
    print(c)
print("\n")

# practise time

favFoods = ["cheeseburger","pizza","kebab"]
for foodItem in favFoods:
    print(foodItem)

print("\n")
for n in range(1,31,2):
    print(n)


print("\n------------------------------------------------------------------While Loops")

a = 1
while a < 5:
    print(a)
    a+=1

x = "Hello World"
y = 1
while y <=3:
    print(x)
    y+=1


b = 0
while b < 10:
    b+=1
    if b == 7:
        continue # continues through the loop omitting the instance in which the condition was met
    print(b)

print("\n")

c = 0
while c < 50:
    c +=3
    if c == 45:
        break # breaks from the loop at the point the condition is met
    print (str(c)+" looping.....")
# remember indentation is important in python
print("you have reached the end of the loop")

# Nesting for loops - a loopception. a loop within a loop
print("\n")
outerLoop = ["1","2","3"]
nestedLoop = ["a","b","c"]

for loopx in outerLoop:
    for loopy in nestedLoop:
        print(loopx,loopy)
print("\n")

numbers = [1,2,3,4,5,6,7,8,9]
letters = ["a","b","c","d","e","f","g","h","i"]

for num in numbers:
    print(num)
    for letter in letters:
        print(letter)
    print("\n")

#practise time
listA = ["1","2","3"]
listB = ["a","b","c","d","e"]

for a in listA:
    print(a)
    for b in listB:
        print(b,listA,listB)
    print("\n")


departments = ["Marketing","Design","Development","Art"]
animals=["monkey","cow","dog","sheep","gorilla","zebra","horse","pig"]

for x in departments:
    print(x)
    for y in animals:
        print(y)
    print("\n")

