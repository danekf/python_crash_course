def get_age():

  try:
    age = int(input('Age please: '))
    print(age)

  except ValueError:
    print('Invalid age, please enter your age in numbers. ')
    get_age()


get_age()
