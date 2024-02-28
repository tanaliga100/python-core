# VARIABLES
name  = "jordantanaliga100"
dan_age = 21
is_active = False
average = 3.3

# CONCAT VARIABLE *can use str method of string to string 
print("Hello ",name, "you are " + str(dan_age))
print(name.upper().__len__())

#OPERATIONS *mathematical
print(10 + 20)
print(30 - 20)
print(10 * 20)
print(20 % 10)
print(abs(323.012300))
print(pow(3, 2))
print(max(2, 1))
print(min(2, 1))
print(round(35.5))

# IMPORT EXTERNAL LIBRARY
from math import *;
print(floor(3.2))


# HANDLE USER INPUT *repl MODE
# nameInput = input("Enter a name : ")
# ageInput = input("Enter a age : ")

# num1 = input("Enter a number : ")
# num2 = input("Enter second number : ")
# result = int(num1) + int(num2)


# print("Hellow " + nameInput.upper() + " your age is : " + ageInput)
# print(result)

# LIST * collections 
price = [231, 12, 5]
fruits = ["mango", "apple", "banana", "apple"]
fruits.extend(price)
print(fruits)
fruits.append("pineapple")
fruits.insert(0, "coconut")
fruits.pop()
print(fruits)
print(fruits.count("apple"))
fruits.reverse()
print(fruits)
fruits2 = fruits.copy()
print(len(fruits2))



# TUPLE * constants collection of lists
coordinates = (3, 5)
print(coordinates[1])


# FUNCTIONS *prefix with a word "def"
def hi(name, age):
  return "Hello "+ name
print(
hi("iza100", 21)
)
def Cube(num):
  return num*num*num
print(Cube(3))

# IF STATEMENTS *need identations
is_yellow = False
is_soft = False
if is_yellow and is_soft:
  print("Hinog na ")
elif is_yellow and not is_soft:
  print("Pahinog na")
else:
  print("Hilaw pa")
  

# DICTIONARIES *like OBJECTS in Javascript
person = {
  "name": "iza100",
  "age": 21,
  "bday": "August 20, 1999",
  "blood_type" : "AB",
  "is_good": True
  
}
print(person.get("surname", "Not a valid key"))
print(person["is_good"])

# LOOPS
# while loop
i = 1
while(i <= 10):
  print(i)
  i += 3
# for-loop * traditional
ints = ["guitar", "piano", "drums"]
for x in ints:
  print(x)
  
  
# TRY CATCH 
while True:
  try:
    n = input("Enter a num: ")
    print(int(n))
    break
  except ValueError:
    print("Invalid input: please Enter a number")
print(n +" IS A NUMBER")
  
  