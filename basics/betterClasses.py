class Point:
  #constructor
  def __init__(self, x, y):
    self.x = x
    self.y = y  

  def move(self):
    print('moving')

  def draw(self):
    print('drawing')


#creates new Point with name
point1 = Point(10,20)

print(point1.x, point1.y)
