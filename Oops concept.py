from enum import nonmember
"""class students:
    Name = None
    Register_number = None
    standard = None
    phone_number = None
    def __init__(self, Name, Register_number, standard , phone_number):
        self.Name = Name
        self.Register_number = Register_number
        self.standard = standard
        self.phone_number = phone_number
        print("Name:", self.Name)
        print("Register_number:", self.Register_number)
        print("standard:", self.standard)
        print("phone_number:", self.phone_number)
a = students("Stephenraj","C22UG154CSC023","Final year","8838260257")
"""

"""class Bike:
    brand = None
    model = None
    color = None
    price = None
    fuel = None
    def Bike(self):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.fuel = fuel
        print("brand:", self.brand)
        print("model:", self.model)
        print("color:", self.color)
        print("price:", self.price)
        print("fuel:", self.fuel)
        print("END".center(25,"*"))
B = Bike()
B.brand="Pulsar"
B.model="Ns"
B.fuel="petrol"
B.color="Red"
B.price=135000
print("brand :",B.brand)
print("model :",B.model)
print("color :",B.color)
print("price :",B.price)
print("fuel :",B.fuel)
"""

'''
import math

# ---------------- Level 1 ----------------

# 1 Student Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul",20)
s2 = Student("Arun",22)

print(s1.name, s1.age)
print(s2.name, s2.age)


# 2 Car Class
class Car:
    def __init__(self):
        print("Car created")

c1 = Car()


# 3 Employee Class
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

e1 = Employee(101,50000)
print(e1.emp_id, e1.salary)


# 4 Book Class
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show_details(self):
        print("Title:",self.title)
        print("Author:",self.author)

b1 = Book("Python Basics","John")
b1.show_details()


# 5 Calculator Class
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print("Sum:",self.a + self.b)

cal = Calculator(10,20)
cal.add()


# ---------------- Level 2 ----------------

# 6 BankAccount
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Balance:",self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        print("Balance:",self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)


# 7 Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

r = Rectangle(10,5)
r.area()


# 8 Laptop Object Counter
class Laptop:
    count = 0

    def __init__(self):
        Laptop.count += 1

l1 = Laptop()
l2 = Laptop()
l3 = Laptop()

print("Total laptops:",Laptop.count)


# 9 Mobile Class vs Object Variable
class Mobile:
    brand = "Samsung"

    def __init__(self,model):
        self.model = model

m1 = Mobile("S21")
m2 = Mobile("A50")

print(m1.brand, m1.model)
print(m2.brand, m2.model)


# 10 Student Age Validation
class StudentAge:
    def __init__(self,age):
        if age >= 18:
            print("Valid Age")
        else:
            print("Invalid Age")

st1 = StudentAge(20)
st2 = StudentAge(16)


# ---------------- Level 3 ----------------

# 11 ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        self.items.remove(item)

cart = ShoppingCart()
cart.add_item("Phone")
cart.add_item("Laptop")
cart.remove_item("Phone")

print(cart.items)


# 12 Temperature Conversion
class Temperature:
    def __init__(self,celsius):
        fahrenheit = (celsius * 9/5) + 32
        print("Fahrenheit:",fahrenheit)

t = Temperature(30)


# 13 Employee Auto ID
class EmployeeAuto:
    count = 100

    def __init__(self):
        EmployeeAuto.count += 1
        self.emp_id = EmployeeAuto.count

emp1 = EmployeeAuto()
emp2 = EmployeeAuto()

print(emp1.emp_id)
print(emp2.emp_id)


# 14 Distance Between Points
class Point:
    def __init__(self,x1,y1,x2,y2):
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        print("Distance:",distance)

p = Point(2,3,5,7)


# 15 Destructor Example
class Person:
    def __init__(self,name):
        self.name = name
        print("Person created")

    def __del__(self):
        print("Person deleted")

p = Person("Rahul")'''