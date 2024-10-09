# lists are just what pythons call arrays
# remember that arrays start with an index of 0!

# Creating Lists
#---------------
people = ["john", "david", "michael", "bishop", "megan", "fido", "charlie"]
print(people)
print(people[3] + " is at the index of 3") # should print out bishop and concatenate the string

#practise
rtsGames = ["StarCraft", "Dawn of War", "Command & Conquer", "StormGate", "Halo Wars"]
print(rtsGames)
print(rtsGames[1],rtsGames[3])
print(rtsGames[2],(type(rtsGames[2])))

# Modifying Lists
#----------------
rtsGames = rtsGames + ["Starship Troopers"]
print(rtsGames)

# + operator can also concatenate two lists together
print(rtsGames + people)

# inserting to a list
rtsGames.insert(2, "War of the Worlds")
rtsGames.insert(5, "Dungeon Keeper")
print(rtsGames)

# removing from a list
del rtsGames[0] #removing starcraft from the list
print(rtsGames)
print(rtsGames[0]) #now the index of 0 is dawn of war

people.remove("bishop")
print(people)

# looping through a list
dogs = ["yorkshire terrier","german shepherd", "daschund","pom-pom", "akita","beagle", "spaniel"]
for breeds in dogs:
    print(breeds)

if "akita" in dogs:
    print("The akita is in the list")

# length of an array/list
print(len(dogs))

#practise
print (" Practise Time")
print("---------------")
produce = ["carrots", "apples","plums","figs","tomatoes"]
print(produce)
produce[3] = "Potatoes"
print(produce)
del produce[2]
print(produce)
produce.insert(3, "Cauliflower")
print(produce)

# Sorting and Reversing Lists
#----------------------------

colors = ["blue","red","yellow","green"]
colors.sort()
print(colors)

print("-------------------------------------------------------")

print(colors)
colors.sort(reverse=True)
print(colors)
#going back and forth using reverse methods
colors.reverse()
print(colors)

# Sorted Function
print(colors)
colors.insert(4, "indigo")

print("\nHere is the first list")
print("-------------------------")
print(colors)

print("\nHere is a sorted list")
print("-------------------------")
print(sorted(colors))
print(colors)
print("notice how the colors resort back to the original order it was written in the list")
print("Whilst the .sort() method is permanent change to the list!")
#practise time
print("\n")
books = ["A day at the zoo","run baby run","Mountain Explorer","Captain Marling","Frankenstein","Gullivers Travels","Gangsters Tale","Sherlock Holmes"]

books.sort()
print(books)
books.reverse()
print(books)

print("\n")

numbs = ["3","7","9","4","5","8","0","1","6","2"]
print(numbs)

numbs.sort()
print(numbs)

# Slicing lists

players = ["player one","player two","player three","player four","player five","player six","player seven"]
print("Here are the current players")
print(players)
for player in players[:3]: # counts up to three in the index. Dont forget the follow up semi-colon for the for loop
    print(player.title())
print("\n")
for player in players[2:5]:
    print(player.title())