
def greet_user(user):
  print(f'Hello {user}')
  print('Lets get coding')
  

name = input('What is your name? ')
greet_user(name)

#Keyword arguments, positiong doesnt matter
def greet_user_key(first, last):
  print(f'Hello {first} {last}')
  print('Lets get coding')
  

f_name = input('What is your first name? ')
l_name = input('What is your last name? ')

greet_user_key(last = l_name, first = f_name)


#returns in python are the same as most other languages

def square(num):
  return num * num

print(square(2))