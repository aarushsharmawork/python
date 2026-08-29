
#list
# we can edit list unlike string
hello = [1 , "aarush", 2.34 , "hoo" , True , None] # we can add multiple variable in string
print(hello[1:4])
hello.append("kiwi") #append means adding to the existing list
print(hello)
#listing method
L1 = [1 , 2 , 45 , 645, 21]
L1.sort() # will sort the value from low to high
#similarly we can also use
# L1.reverse() will reverse the list
# L1.remove() will remove the value completely
# L1.pop(3) it will popout the specfic value of that index and print or perforn fn with that value
# L1.insert(2 , 50) 
# the diff btw insert and append is just that in append value we inserted comes in last 
# while in instert we can add to our desired index in the list
print(L1)

#Tupples
# so tupples are non editable type variables used to store data
tup = (1 , 2 , 3 , 4)
print(type(tup))
print(tup.count(2)) # it will count no of 2 in tupple
print(tup.index(3)) # will find the value and will tell at which index it is
print(len(tup)) # will tell how many no of element are present
print(min(tup)) # will return min value of tupple
print(max(tup)) # will return max value of tupple
print(sum(tup)) # will return the sum of tupple
print(3 in tup) # will return the boolean in tupple
print(5 in tup) # will return the boolean in tupple
print(tup[0]) # will return the index value in tupple
print(tup[-1]) # will return the index value in tupplet
print(tup[1:3]) # will give the value btw 1 and 3 excluding 3

#Dictionary
d = { "aarush" :80,
     "rohan" :34,
     "ayush" :50,
     "rohit" :30,} # // Dictionary has two variable one is key and other is value
# // on the left keys are written on the right values are written in dictionary
# // key is usually stored in the form of commutable element ie str int flt or tupple or bln
# // value can be of any type
d.update({"abhay" :43,
         "bhavya" :67 }) # // update Dictionary with new audition

print(d ["aarush"]) # //print the value of the key Aarush
# print(d [34]) //considered wrong as we can only find value from keys only
print(d.items()) # // print items in the form of tuples
print(d.keys()) # // print keys
print(d.values()) # // print values
print(len(d)) # To find length of d
d.pop("rohan")  # Removes the given key and returns its value
d2 = d.copy()  # Creates a copy of the dictionary
d2.popitem()   # Removes and returns the last inserted key-value pair
# d2.clear()  # Removes all key-value pairs from the dictionary
d.setdefault("rahul", 40)   # Returns the value if the key exists, otherwise adds the key with the given default value
print(d) # //print the key and values in Dictionary
print(d2)

# Creating dictonary search feature
words = { "help": "madad",
         "hello": "namaste",
         "name": "naam"}
word = input("enter word you want to search ") # this is another variable from above
print(words[word])
#Sets
# sets are the variables in which only value can be stored
#sets are unordered so they don't have index
s = {1, 2 , 3, 5, 4, 5, 6} # in sets the same values can only be written once else it would not consider the repeated value
s.add("aarush") # we can use this to add other values to set
s.remove(6) # remove the value of a set give an error if element not found
s.discard(10) # Removes the given element (does not give an error if not found)
# s.pop() remove random value from set
# s.clear() clear all values from set
print(len(s))
print (s, type(s)) # to print set s and print data type of set
s2 = s.copy() # Creates a copy of the set
s1 = {23, 45 ,56, 44}
s2 = {22, 45, 65, 34}
print (s1.union(s2)) # print the union value of 2 sets
print (s1.intersection(s2)) # print the intersection value of 2 sets
print(s1.difference(s2)) # returns value of first set that are not present in 2nd set
print(21 in s1) # finds wether the given value is present in set by boln
print(5 not in s1) # finds wether the given value is present in set by boln
print(s1.issubset(s2))
s1  -s2 # print the intersection value of 2 sets
