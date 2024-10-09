import os
# Merging
# the with statement automatically closes the files

with open("hello.txt","w") as file:
    file.write("hey there!")

with open("names.txt","r") as n_file:
    with open("messages.txt","r") as m_file:

        body = m_file.read()
        for name in n_file:

            mail = "hello"+name+body
            with open(name.strip()+".txt","w") as m_file:
            
                m_file.write(mail)

with open("mergeFile.txt","r+") as mergy:
    mergy.write("Do you need to write something. Because an empty txt file is not readable?")
    print(mergy.read())
    mergy.close()

os.remove("bazil.txt")
os.remove("bob.txt")
os.remove("dave.txt")
os.remove("elenor.txt")


