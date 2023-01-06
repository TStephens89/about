from collections import namedtuple
Pen = namedtuple("Pen", "size inkcolor beveled")

standardPen = Pen(2, "black", True)
bigPen = Pen(25, "black", True)
idkPen = Pen(10, "black", True)

print(bigPen, idkPen, standardPen)

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=2, y=1)
p2 = Point(x=4, y=7)

x, y = p1
x, y = p2

def slope(p1,p2):
 return (p2.y - p1.y) / (p2.x - p1.x)
  
  
print(slope(p1,p2))