# class Person:
#   name = "Trevor" 
#   age = 33
#   def intro(self):
#     print(f"my name is {self.name} and I am {self.age} years old")
# trevor_person = Person()
# print(trevor_person)
# trevor_person.intro()

# class Cat:
#   def __init__(self, name, breed, age):
#     self.name = name
#     self.breed = breed
#     self.age = age
# new_cat = Cat("Sasha", "Street Cat", 3)

# print(new_cat.age)

# class Person:
#   def __init__(self, first_name, last_name):
#     self.first_name = first_name
#     self.last_name = last_name
#   class Coach(Person):
#     def __init__(self, first_name, last_name, cohort)

class Wallet:
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit
  
  def __str__(self):
    return f"{self.value} {self.unit}"
    
  def __add__(self, value2):
    return Wallet(self.value + value2.value)

my_wallet = Wallet(5000)
another_wallet = Wallet(100)
third_wallet = my_wallet + another_wallet

# print (another_wallet)

# print(my_wallet.value)
print(third_wallet.value)