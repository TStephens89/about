# multiplication table

for x in range (1, 11):
    for y in range (1, 11):
        print ('{:6}'.format(x*y), end=' ')
    print()

# dictionary practice

my_dictionary = { "Barack Obama": "USA", "Thomas Jefferson": "USA", "Vladimir Lenin": "Russia", "Tsar Nicolas III": "Russia", "John Curtin": "Austrailia"}

print("Barack Obama is from", my_dictionary["Barack Obama"])

customers = [] 
while True: 
  user_input = input("Enter another name?: (Yes/No) ") 
  user_input = user_input[0].lower() 
  if user_input == "n": 
    break 
  else: 
    first_name, last_name = input("Enter your name (first/last): ").split() 
    customers.append({"first name": first_name, "last name": last_name}) 
for c in customers: 
  print(c["first name"], c["last name"])
  
# FizzBuzz between 1-200

for i in range(1,200):
  if i % 3 == 0 and i % 5 == 0:
    print ("FizzBuzz")
  elif i % 3 == 0:
    print ('Fizz')
  elif i % 5 == 0:
    print ('Buzz')
  else:
    print (str(i))

