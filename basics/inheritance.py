class Animal:
  def walk(self):
    print('walk')


#inherit stuff from animal
class Dog(Animal):
  def bark(self):
    print('bark')


class Cat(Animal):
  def meow(self):
    print('meow')



rudy = Dog()
rudy.walk()

kerrigan = Cat()
kerrigan.meow()