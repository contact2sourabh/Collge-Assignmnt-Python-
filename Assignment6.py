#%%
#tuple:operation1

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#%%
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#%%
#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#%%
#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  #%%
  #Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  #%%
#Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#%%
#You cannot add items to a tuple
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)
#%%
#Create Tuple With One Item
#One item tuple, remember the commma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#%%
#Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#%%
#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#%%
#Count()
#Return the number of times the value 5 appears in the tuple:

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
#%%
# Index(): Search for the first occurrence of the value 8, and return its position:

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
#%%

#SET
#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)
#%%
#Operation1: Add an element to the fruits set:

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)
#%%
#Remove all elements from the fruits set:

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)
#%%
#Copy the fruits set:

fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)
#%%
# Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)
#%%
#Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#%%
#Return True if no items in set x is present in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
#%%
#Return True if all items set x are present in set y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
#%%
#Remove a random item from the set:

fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)
#%%
#Return a set that contains all items from both sets, duplicates are excluded:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
#%%
#Insert the items from set y into set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)
#%%
#Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#%%
#Get the value of the "model" key:

x = thisdict["model"]

#%%
#Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#%%
#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#%%
#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#%%
#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#%%
#The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict
#%%
#Ques3:
fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)

lst = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)

#%%
#%%
#%%