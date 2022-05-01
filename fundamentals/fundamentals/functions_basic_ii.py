#1. Countdown

def coundown(a):
    b = []
    for i in range(a, -1, -1):
        b.append(i)
    return b
print(countdown(5))

#2. Print and Return

def print_and_return(a):
    print(a[0])
    return a[1]
print(print_and_return([1,2]))

#3. First plus Length

def first_plus_length(a):
    return a[0] + len(a)
print(first_plus_length([1,2,3,4,5]))

#4. Values Greater than Second

def values_greater_than_second(a):
    
    if len(a) < 3:
        return False
    new = []
    y = 0
    while y < len(a):
        if a[y] > a[1]:
            new.append(a[y])
        y += 1
    print(len(new))
    return new
print(values_greater_than_second([5,2,3,2,1,4]))

#5. This Length, That Value

def length_and_value(a,b):
    new = []
    while len(new) < a:
        new.append(b)
    return new

print(length_and_value(4,7))
print(length_and_value(6,2))