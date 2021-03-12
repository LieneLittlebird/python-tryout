# A collection which is unordered, changeable and indexed. No duplicates
# Similar to object literal

# Create a dictionary - an object in JS
person = {"first_name": "John", "last_name": "Doe", "age": 30}
print(person, type(person))

# Use constructor
# person2 = dict(first_name = "Sara", last_name = "Williams")

# print(person2, type(person2))

# Get value
print(person["first_name"])  # More common
print(person.get("last_name"))

# Add key/value
person["phone_number"] = "555-555-555"

print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy a dict
person2 = person.copy()
person2["city"] = "Boston"

print(person2)

# Remove item
del person["age"]
person.pop("phone_number")

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [{"name": "Martha", "age": 30}, {"name": "Kevin", "age": 25}]

print(people[1]["name"])
# print(person)
