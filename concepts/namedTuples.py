from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=11, y=22)

print(type(Point))

print (p[0])
print (p[1])

x, y = p
print(x,y)

print(p.x, p.y)

EmployeeRecord = namedtuple("EmployeeRecord", "name age title")

empl_rec = EmployeeRecord("Michael Corleone", 45, "The GodFather")

print(f"{empl_rec.name} is the new {empl_rec.title}")

Parent = namedtuple("Parent", "name children")

vito = Parent("Vito Corleone", ["Sonny", "Michael"])

print(vito.children)

Developer = namedtuple("Developer", "name level language", defaults= ["Junior", "Python"])

dev = Developer("Steve", "Senior")

print(f"{dev.name} is a {dev.level} developer in {dev.language}")

Person = namedtuple("Person", "name age height")
Person._make(["John", 25, 72])

joe_bob = Person("Joe Bob", 33, 72)


print(joe_bob._asdict())