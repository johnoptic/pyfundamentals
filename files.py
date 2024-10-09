import shutil
import os

# Copying Files
#shutil.copy(src,dst)
#shutil.copystat(src, dst) - CopyStat is used to copy a file with MetaData information
src = "demo.txt"
dst = "Johnsdemo.txt"

shutil.copy(src,dst) # copys the source txt onto the destination text

# Renaming Files
os.rename("Johnsdemo.txt", "changedName.txt")

# Deleting Files
os.remove("changedName.txt")

x = open("xfiles.txt","a")
x.write("Here is a line of text\n")
x.write("Here is another line of text \n")
x.close()
shutil.copy("xfiles.txt","demo.txt")

x = open("xfiles.txt","a")
x.write("Here is one more line of code\n")
x.close()
z = open("demo.txt")
x = open("xfiles.txt")
print(x.read() + "\n")
print(z.read())
x.close()
z.close()
