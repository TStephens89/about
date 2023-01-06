import math
class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width

  @property
  def height(self):
    return self._height

  @property
  def width(self):
    return self._width

  @height.setter
  def height(self, new_height):
    self._height = new_height

  @width.setter
  def width(self, new_width):
    self._width = new_width
  
  def area(self):
    return self.height * self.width
        
newRectangle = Rectangle(25, 55)

def main():
  print("height = ", newRectangle._height)
  print("width = ", newRectangle._width)
  print("area = ", newRectangle.area())
  
if __name__ == "__main__":
  main()
  
class Vehicle:
    def __init__(self, name = ""):
        self.name = name
        
    def useGas(self):
        print("There are many kinds of Vehicles. Some Vehicles use gas. Some cannot.")
        
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        
    def useGas(self):
        print(f"A {self.name} can use gas.")
        
class Tesla(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        
    def useGas(self):
        print(f"A {self.name} cannot use gas.")
        
Vehicle = Vehicle()
Car = Car("F-150")
tesla = Tesla("Tesla")

def main():
    Vehicle.useGas()
    Car.useGas()
    tesla.useGas()

    
if __name__ == "__main__":
    main()
  
