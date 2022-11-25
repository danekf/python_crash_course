#playing app, to show differences in python that are useful to remember. This is just a reference

######## MISC ############


#multiplication on a string, works in python
print('*' * 10) 

#variables dont have a declaration in python, they are inferred
price = 10
cad_tax_multiplier = 1.13

print(round(price * cad_tax_multiplier, 2),'$')

#can use 3 quotes to have multiple lines for a string
message = '''Hello,
Welcome to python.

Have fun you silly goose.'''

print(message)

#can use negative integers to get characters starting FROM THE END.
#0 is always start point, so to get last character, use -1
print(message[-1]) #returns the period

#can extract a few up UNTIL the last index
print(message[0:4])





######## STRINGS ############

#formatted strings
first_name = 'Danek'
last_name = 'Fill'

msg = f'{first_name} {last_name} is a coder.'
print (msg)

#length
print(len(first_name))

#uppercase
print(first_name.upper())

#find index of, case sensitive, -1 is not found
print(first_name.find('e'))
print(message.find('python'))

#replace
print(message.replace('python', 'the chicken factory'))

#find using IN, returns bool
print('python' in message)




######## ARRAYS ############

numbers = [5,2,4,7,4]

#copy
numbers2 = numbers.copy()

#append (add to end)
numbers.append(13)
print(numbers)

#insert (add to specific point)
numbers.insert(2, 5)
print(numbers)

#remove (remove FIRST INSTANCE number from array)
numbers.remove(5)
print(numbers)
numbers.remove(5)
print(numbers)

#index (show first instance of item)
print(numbers.index(2))
#alternatively use IN to check for existence of
print(50 in numbers)


#pop (remove last item)
numbers.pop()
print(numbers)

#sorting
numbers.sort()
print(numbers)

#reverse
numbers.reverse()
print(numbers)


#clear (remove all from list)
numbers.clear()
print(numbers)