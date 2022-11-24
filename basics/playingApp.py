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

