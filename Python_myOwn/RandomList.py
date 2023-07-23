import random

# random number b/w 0 and 15
print(f"random number b/w 0 and 15: {random.randrange(15)}")

# random number b/w 10 and 100
print(f"random number b/w 10 and 100: {random.randint(10, 100)}")

myList = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii"]
# make List non-sequential and random
random.shuffle(myList)
print(f"make List non-sequential and random: {myList}")

myList = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii"]
# get an item from list randomly
print(f"get an item from list randomly: {random.choice(myList)}")

# get sub List from list  of random items
print(f"get sub List from list  of random items: {random.sample(myList,3)}")

