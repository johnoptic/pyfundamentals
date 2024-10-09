# Handling exceptions
import sys

try:
    print(0/0)
except ZeroDivisionError:
    print("You cannot divide by Zero!")

try:
    number = int(input("Enter a number betwenn 1 - 10"))
    print("you entered the number",number)
except ValueError:
    print ("Please use numbers only. Thank you!")
    sys.exit() # forces program to stop gracefully after the error


