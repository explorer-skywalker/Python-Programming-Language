
# Commenting the code;
  #-> Comment the code for understanding & for future reference
  #-> Ctrl + /   ; To comment a whole line

print('hello world')   # Comment after code

'Refered as string comment'
"Refered as string comment"

'''
Refered
as
string
comment

'''

"""
Refered 
as
string
comment

 WOW
 0 0
  ^
 ---

"""

# docstring?



# Exercise: Password Checker
username = input('Enter Username; ')
password = input('Enter Password; ')
print(f"\nYour Username; {username}\nYour Password; {'X' * len(password)}\nYour Password Strength;", len(password))



# Lists
list
list1 = ["anything", 1, 2, 3, 'helllo world', 3.33, 9.63, True, False]
print(list1)
print(*list1, '\n')   # Args, Unpacking

  # Data Structures; like a backpack

list
amazon_cart = ['Rasberry PI 4', 'Acer Monitor', 'RGB Keyboard & Mouse', '500GB NVMe PCIe SSD']
print(amazon_cart)
print(*amazon_cart)
print(amazon_cart[0])   # Index
print(amazon_cart[3])
print(amazon_cart[2])



# List Slicing
  #-> Just like string slicing
  #-> Unlike strings, List is mutable means, we can change the list's value
  #-> After updating lists, it creates a new list with updated values
list
amazon_wishlist = [
              'Rasberry PI 4', 
'Acer Monitor', 
'RGB Keyboard & Mouse', 
      '500GB NVMe PCIe SSD', 
'8GB RAM 2666MHz for Thinkpad E14'
'Laptop stand'
]
print(amazon_wishlist)
print(amazon_wishlist[0:5:1])   # list slicing [start:stop:skip]
print('\n')

amazon_wishlist[0] = 'Rasberry PI 4 Tool Kit'   # list is mutable, it can be modifed/updated
print(amazon_wishlist, '\n')

amazon_wishlist2 = amazon_wishlist[0:3]   # Copying, it creates a copy of actual list
print(amazon_wishlist2)
print(amazon_wishlist, '\n')   # Actual list is safe

# Important Concept
new_wishlist = amazon_wishlist2   # Modifying, because it points to actual list
new_wishlist[0] = 'Macbook Pro'
print(amazon_wishlist2)   # Actual list changed



# Matrix;
  #-> lists under list or sub-lists under list or onion/tor
list
  #-> list are also called array in other programming languages

matrix = [
[1, 2, 3],
['matrix1', 'matrix2', 'matrix3'],
[3, 6, 9],
[333, 666666, 999999999 ]
]
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[1][0])
print(matrix[1][2])



# List Methods;
list
ai = [
  ['Artificial Intelligence',['Machine Learning',['Deep Learning']]],
  ['Data Science',['Handling & Analysis of Data ']]
]
print(*ai)

  # len() method
print(len(ai))   
print(ai[0][1][0])

  # append()
sai = ai.append('Super Artificial Intelligence')   # pointer, sai points on ai
print(sai)
print(*ai, '\n')

  # insert()
droid = ai.insert(1, 'Robots, C-3PO, R2-D2, L3, K2, Android')   # pointer, modifies the pointed list[]
print(droid)   # pointer, none
print(*ai, '\n')

  # extend()
features = ai.extend(['Voice clearity, Better Graphics, Smarter than before'])
print(features)   #None
print(*ai, '\n')

  # pop(), Remove by specifying the Index

ai.pop()   # removes the last value by default
print(ai, '\n')

poped_value = ai.pop(1)   # removes the specifed index value 
print(poped_value)   # Returns the poped values
print(ai, '\n')

  # remove(), Remove by specifying the Value
removed_value = ai.remove('Super Artificial Intelligence')
print(removed_value)
print(*ai, '\n')

  # clear()
cleared_list = ai.clear()   # Clears the whole list, yeahhh..
print(cleared_list)
print(ai)



# List Methods 2;
list
basket = ['sweets', 'chocolates', 'fruits', 'vagetables', 'notebook', 'pen', 'stick', 'pen', 'e-pen']
print(basket)

  # index()
print(basket.index('pen'))   # Index location of any value
print(basket.index('pen', 0, 6))   # search limit, (value, start, stop)

  # keyword, ' in '
print('notebook' in basket)
print('laptop' in basket)

  # count()
print(basket.count('e-pen'))
print(basket.count('pen'))   # Frequency of any value in list



# List Methods 3;
list
  # sort()
keys = ['a', 's', 'd', 'f']
sort_keys = keys.sort()   # Sort in alphabetic manner
print(sort_keys)
print(keys)

sort_basket = basket.sort()   
print(sort_basket)
print(basket)

  # sorted(), Creates a new list rather than modifying it !
basket2 = ['sweets', 'chocolates', 'fruits', 'vagetables', 'notebook', 'pen', 'stick', 'pen', 'e-pen']
sorted_list = sorted(basket2)
print(sorted_list)   # Actual sorted list
print(basket2)

  # copy()
copy_list = basket2.copy()    # or, [:]  to copy
print(copy_list)   # Clone of basket2

  # reverse()
reverse_list = basket2.reverse()    # reverse the values, as said !
print(reverse_list)
print(basket2)

  # sort() & reverse() 
basket3 = ['sweets', 'chocolates', 'fruits', 'vagetables', 'notebook', 'pen', 'stick', 'pen', 'e-pen']
basket3.sort()      # points on actual list
basket3.reverse()   # points on actual list
print(basket3)



# Common List Patterns;
list
  # reverse methods
basket = ['x', 'a', 's', 'd', 'f', 'j']
basket.sort()
basket.reverse()
print(basket[::-1])   # Creates a new copy of itself
print(basket)

  # range(start, stop)
print(list(range(3, 99)))   # As directed
print(list(range(101)))   # 0 to Maximum, whole numbers

  # join()
sentence = ' '
new_sentence = sentence.join(['I', 'am', 'Captain'])   # Creates new list
print(new_sentence)

print(" ! ".join(['Hello', 'Captain']))



# List Unpacking;
list
  # *Variable-Name
a, b, c, *other, d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print(a)
print(b)
print(c)
print(other)
print(d)
print(e)



# None;
None 
  # None represents the absence of value
  # In other programming languages, None = Null also !
gamer1_weapon = None
print(gamer1_weapon)



# Dictionary;
dict
  # Dictionary is an unordered key-value pairs
dictonary1 = {
  'a': [1, 2, 3],
  'b': 'hello',
  'c': True,
  'first_program': 'Hello World'
}
print(dictonary1)
print(dictonary1['a'])
print(dictonary1['b'])
print(dictonary1['c'])
print(dictonary1['first_program'])

  # Typecasting dict into list for using index order
mylist = [
  {
  'a': [1, 2, 3],
  'b': 'hello',
  'c': True,
  'first_program': 'Hello World'
  },
  {
  'num1': 1,
  'num2': 2,
  'num3': [1, 2, 3]
  }]

print(mylist)
print(mylist[0])
print(mylist[0]['first_program'])

print(mylist[1])
print(mylist[1]['num3'])













