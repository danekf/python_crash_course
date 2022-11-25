class Point:
  

  def move(self):
    print('moving')

  def draw(self):
    print('drawing')


#creates new Point with name
point1 = Point()

#can assign attributes to point using .notation anywhere in the program if needed. but constructors are better, see better classes

point1.x = 10
point1.y = 20

print(point1.x)
print(point1.y)
point1.draw()

