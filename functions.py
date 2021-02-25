# Create a function
# In Python we use tabs and spaces instead of curly brackets
def sayHello(name="Sam"):  # Add a default name
    print(f"Hello {name}")

# sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

num = (getSum(3, 4))
# print(num)

#Lambda function - a small anonymous function. 
# Can take in any number of arguments, but has only one expression.
#Similar to arrow functions in JS

getSum2 = lambda num1, num2: num1 + num2;

# print(getSum(10, 3));


