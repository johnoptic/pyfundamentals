# Input() by default converts all the information it recieves into a string
# This means that handling numbers means we have to be explicit about the datatypes

text = input("Can you see this? yes or no?")
print("you wrote" + text)

# numbers

txt = input("Give me a number:")
num = int(txt)
print("the number you gave is:", num)

# another method of writing this

prompt = int(input("What is this?"))
print("The number you gave is: ",prompt)

# Input Errors
a=input("Can i Have a number please?")
try:
    b=int(a)
    print("the number you have given is: ",b)
except ValueError:
    print("please put in a real number, not a string")

