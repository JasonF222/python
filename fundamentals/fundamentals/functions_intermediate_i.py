1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 

def valChange(z):
    z[1][0] = 15
    return z

print(valChange(x))

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

def studentChange(z):
    z[0][3] ="Bryant"
    return z

print(studentChange(students))

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def directoryChange(z):
    z['soccer'][0] = "Andres"
    return z

print(directoryChange(sports_directory))

z = [ {'x': 10, 'y': 20} ]

def changeY(a):
    a[0]['y'] = 30
    return a

print(changeY(z))


2. Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(a):
    for x in a:
        for keys in x.keys():
            print(keys + " - " + x[keys]) 

print(iterateDictionary(students))

3. Get Values From a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    count = 0
    while count < len(some_list):
        for key in some_list[count]:
            print(some_list[count][key_name])
            count += 1

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

4. Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for z in some_dict:
        print(len(some_dict[z]), z)
        for x in range(0, len(some_dict[z])):
            print(some_dict[z][x])

printInfo(dojo)
