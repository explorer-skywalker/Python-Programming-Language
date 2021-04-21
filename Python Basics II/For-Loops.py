
# for loops;
for item in "Captain Skywalker":    # it creates a variable - item
    print(item)

for item in '1234567890':
    print(item)

for item in [369, "hello", True, 1319]:     # works with different datatypes also
    print(item)

for item in {369 : "hello", True : 1319}:    
    print(item)

for item in (369, "hello", True, 1319):    
    print(item)

    # Matrix / loop under loop
for item in [369, "hello", True, 1319]:    
    for x in [1, 2, 3, 4]:
        print(x, item)



# Iterables / Iterate;
    #-> Could be Strings, list[], tuple(), set{}, dict{:}
    #-> Goes one by one to check every item in collection

    # Iterate over dict{:}
user1 = {
    "name" : "Unknown",
    'age' : "Whatever",
    'is_concious' : True
}

for keys in user1:
    print(keys)

   # .items()
for item in user1.items():
     print(item)

    # .keys()
for key in user1.keys():
    print(key)

    # .values()
for value in user1.values():
    print(value)

   # key, value
for key, value in user1.items():
    print(key, value)

   # key-value, f-string
for key, value in user1.items():
    print(f"{key}-{value}")



# Exercise: Tricky Counter ;
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
counter = 0
for item in list1:
    counter = counter + item
print("The sum is", counter)



# range();
range









