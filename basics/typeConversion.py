import datetime
today = datetime.date.today()

#input always returns string
birth_year = input('Enter birth year: ')

#convert str to int then continue
age = today.year - int(birth_year)

#print converted age as string
print('You are ' + str(age) + ' years old.')

