# # 1. TASK: print "Hello World"
# print( "Hello World" )
# # 2. print "Hello Noelle!" with the name in a variable
# name = "Jason"
# print( "Hello ", name, "!")	# with a comma
# print( "Hello" + name + "!" )	# with a +
# # 3. print "Hello 42!" with the number in a variable
# name = 42
# print( "Hello", name, "!" )	# with a comma
# print( "Hello" + str(name) + "!"  )	# with a +	-- this one should give us an error!
# # 4. print "I love to eat sushi and pizza." with the foods in variables
# fave_food1 = "sushi"
# fave_food2 = "pizza"
# print( "I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
# print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string


x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   

