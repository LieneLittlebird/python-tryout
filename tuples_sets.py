#A tuples is a collection that is orderder and UNchangeable. 
#Store multiple values in a single variable
# Allows duplicate numbers

#Create tuple
fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

#Single value needs trailing comma
fruits2 = ("Apples",)

# print(fruits2, type(fruits2))

#Get value
# print(fruits[1])

# #Can't change value
# fruits[0] = "Pears"

#Delete tuple
del fruits2

#Get length
# print(len(fruits))

#Sets - a collection  which is unordered and unindexed. No duplicate members

#Create a set
fruits_set = {"Apples", "Oranges", "Mangoes"}

#Check if in set
print("Apples" in fruits_set)

#Add to set
fruits_set.add("Grapes")

#Remove from set
fruits_set.remove("Grapes")

#Clear set
fruits_set.clear()

print(fruits_set)
