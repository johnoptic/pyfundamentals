# Displaying Daytime 
from datetime import datetime
from datetime import time
from datetime import date # importing classes as well as module

# date - manipulate just the date
# datetime - manipulate the date and time
today = date.today()
date_time = datetime.now()
print("Todays date is: ",today)
print("all together now: ",date_time)

# Working Directory
import os
dirpath= os.getcwd() #get current working directory
print("Your current directory is: " + dirpath)
foldername = os.path.basename(dirpath)
print("The directory name is: " + foldername) 

# File Metadata
print(os.stat("Metadata.py"))

