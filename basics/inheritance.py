class Animal:
  def walk(self):
    print('walk')


#inherit stuff from animal
class Dog(Animal):
  #pass to get passed the empty class.
  pass


class Cat(Animal):
  pass



rudy = Dog()
rudy.walk()