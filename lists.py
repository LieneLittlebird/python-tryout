#Create a list
numbers = [1, 2, 3, 4, 5] #more common
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

#Use constructor
# numbers2 = list((1, 2, 3, 4, 5))

#Get a value

# print(fruits[1])

#Get length
# print(len(fruits))

#Append to  list
fruits.append("Mangos")

# print(fruits)

#Remove from list
fruits.remove("Grapes")

# print(fruits)

#Insert into position
fruits.insert(2, "Strawberries")

#Change value
fruits[0] = "Blueberries"
#Remove from certain positions (pop)
fruits.pop(2)

#Reverse list
fruits.reverse()

#Sort list
fruits.sort()

#Revers sort
fruits.sort(reverse=True)
print(fruits)

