num1 = 42 # variable declaration - data types - primitive - numbers
num2 = 2.3 # variable declaration -data types - primitive - numbers
boolean = True # variable declaration - data types - primitive - boolean
string = 'Hello World' # variable declaration - data types - primitive - string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration - data types - compsite - list - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration - data types - composite - list - initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration - data types - composite - list - initialize
print(type(fruit)) # log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') # variable declaration - data types - composite - list - change value
print(person['name']) #log statement
person['name'] = 'George' # variable declaration - data types - composite - list - initialize
person['eye_color'] = 'blue' # variable declaration - data types - conposite - list - initialize
print(fruit[2]) #log statement

# conditional - if - else
if num1 > 45:
    print("It's greater") 
else:
    print("It's lower")

# conditional - if - else if - else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0

# while loop
while(x < 5):
    print(x)
    x += 1

# data types - composite - list - change value
pizza_toppings.pop()
pizza_toppings.pop(1)

# log statement - data types - composite - list - change value
print(person)
person.pop('eye_color')
print(person)

# for loop - conditional - log statement - conditional
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

# function - for loop - log statement
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

# function - for loop - log statement
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

# function - for loop - log statement
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


# multiline comment
"""
Bonus section 
"""

#single line comment

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)