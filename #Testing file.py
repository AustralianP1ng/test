#Variables

#first_name = "Xuecheng"
#last_name = "Cai"
#full_name = first_name + " " + last_name
#print("Hello " + full_name)

#age = 15
#age += 1
#print("Your age is: " + str(age))

#height = 175.69
#print("Your height is: " + str(height))

#human = True
#print("Are you a human: " + str(human))





#Multiple Assignmen

#name = "Xuecheng"
#age = 15
#attractive = True

#name, age, attractive = "Xuecheng", 15, True

#print(name)
#print(age)
#print(attractive)

#Spongebob = 30
#Squidward = 30
#Sandy = 30
#Patrick = 30

#Spongebob = Squidward = Sandy = Patrick = 30

#print(Spongebob)
#print(Squidward)
#print(Sandy)
#print(Patrick)





#String Methods

#name = "Xuecheng"
#print(len(name))
#print(name.find("X"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha()) #Checks to see if the string only contains alphabetical letters
#print(name.count("e"))
#print(name.replace("e", "a"))
#print(name*3)





#Type cast - convert the data type of a value to another data type

#x = 1   #int
#y = 2.0 #float
#z = "3" #str

#x = float(x)
#y = int(y)
#z = int(z)

#print("X is " + str(x))
#print("Y is " + str(y))
#print("Z is " + str(z))





#User input

#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))

#age = age + 1

#print("Hello " + name)
#print("You are " + str(age) + " years old!")
#print("You are " + str(height) + "cm tall!")





#Maths Functions

#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi, 2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))





#String Slicing - Slicing is creating a substring by extracting elements from another string
#Indexing[] or slice()
#[start:stop:step]

#name = "Xuecheng Cai"

#first_name = name[:8]
#last_name = name[9:]
#funky_name = name[::2]
#reversed_name = name[::-1]

#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#website1 = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7,-3)

#print(website1[slice])
#print(website2[slice])





#if statements - A block of code that will execute if its condition is true

#age = int(input("How old are you?"))

#if age>= 18:
    #print("You are an adult")
#elif age < 0:
    #print("You are an unborn human")
#else:
    #print("You are underaged!")





#Logica operators (amd, or) - used to check if two or more conditional statements are true

#temp = int(input("What is the temperature outside?: "))

#if not(temp >= 0 and temp <= 30):
    #print("The temperature is bad today!")
    #print("Stay inside!")
#elif not(temp < 0 or temp > 30):
    #print("The temperature is good today!")
    #print("Go outside.")





#While loop = A statement that will execute its block of clode as long as its condition remains true

#name = None

#while not name:
    #name = input ("Enter your name: ")

#print("Hello " + name)





#For loop = a statement that will execute its block of code in a limited amount of times
#While loop is unlimited
#For loop is limited

#import time

#for i in range(10):
    #print(i + 1)

#for i in range(50,100 + 1,2):
    #print(i)

#for i in "Xuecheng Cai":
    #print(i)

#for seconds in range(10, 0, -1):
    #print(seconds)
    #time.sleep(1)
#print("Happy New Year!")





#Nested loops - The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

#rows = int(input("How many rows do you want?: "))
#columns = int(input("How many column: "))
#symbol = input("Enter a symbol to use: ")

#for i in range(rows):
    #for j in range(columns):
        #print(symbol, end = '')
    #print()





#Loop control statements = change a loop's execution from its normal sequence

#break = terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acs as a placeholder

#while True:
    #name = input("Enter your name: ")
    #if name != "":
        #break

#phone_number = "123-456-7890"

#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end = '')

#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i, end = '')





#list = used to store multiple items in a single variable

#food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

#food[0] = "sushi"

#food.append("ice cream")
#food.remove("hotdog")
#food.pop()
#food.insert(0, "cake")
#food.sort()
#food.clear()

#for i in food:
    #print(i)





#2D lists (multi-dimensional list) = a list of lists

#drinks = ["soda", "water", "tea"]
#dinner = ["pizza", "hotdog", "steak"]
#dessert = ["cake", "ice cream"]

#List_of_food = [drinks, dinner, dessert]

#print(List_of_food[1][2])





#tuple = collection which is ordered and unchangeable, used to group together related data

#student = ("Xuecheng", 15, "male")

#print(student.count("Xuecheng"))
#print(student.index("male"))

#for i in student:
    #print(i, end= ' ')

#if "Xuecheng" in student:
    #print("Xuecheng is here!")





#Set = collection of which is unordered, unindexed. Does not allow duplicate values

#Utensils = {"fork", "spoon", "knife", "knife", "knife"}
#Dishes = {"bowl", "plate", "cup", "knife"}

#Utensils.add("napkin")
#Utensils.remove("spoon")
#Utensils.clear()

#Dishes.update(Utensils)

#Dinner_table = Utensils.union(Dishes)

#print(Dishes.difference(Utensils))
#print(Dishes.intersection(Utensils))

#for i in Dinner_table:
    #print(i)





#Dictionary = A changeable, unordered collection of unique key:value pairs. Fast because they use hashing. allows us to access a value quickly

#Capitals = {'USA': 'Washington DC',
            #'India':'New Dehli',
            #'China':'Beijing',
            #'Russia':'Moscow'}

#Capitals.update({'Germany':'Berlin'})
#Capitals.update({'USA':'Las Vegas'})

#Capitals.pop('China')
#Capitals.clear()

#print(Capitals['Germany'])
#print(Capitals.get('Germany'))
#print(Capitals.keys())
#print(Capitals.values())
#print(Capitals.items())

#for key,value in Capitals.items():
    #print(key,value)





#Index operator [] = gives access to a sequence's element (str, list, tuples)

#name = "xuecheng Cai"

#if (name[0].islower()):
    #name = name.capitalize()

#first_name = name[0:8].upper()
#last_name = name[9:].lower()
#last_character = name[-1]

#print(first_name)
#print(last_name)
#print(last_character)





#Function = a block of code which is executed only when it is called.

#def Hello(first_name, last_name, age):
    #print("Hello " + first_name + " " + last_name)
    #print("You are " + str(age) + " years old")
    #print("Have a nice day!")

#Hello("Xuecheng", "Cai", 15)





#Return statement = Functions send Python values/objects back to the caller. These values are known as the function's return value

#def multiply(number1, number2):
    #return number1 * number2

#print(multiply(6,8))





#Keyword arguments = arguments preceded by an identifier when we pass them to a function.
#The order of the arguments doesn't matter, unlike positional arguments.
#Python knows the names of the arguments that our function receives.

#def hello(first, middle, last):
    #print("Hello " + first + " " + middle + " " + last)

#hello(last = "Cai", middle = "lol", first = "Xuecheng")





#Nested Function calls = Function calls inside of other function calls
#Inner-most function calls are resolved first
#Returned value is used as argument for the next outer function

#um = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs(float(input("Enter a whole positive number: ")))))





#Variable Scope = The region that a variable is recognized
#A variable is only available from inside the region it is created.
#A global and locally scoped versions of a variable can be created.

#name = "Xuecheng Cai"       #Global scope (available inside and outside functions)

#def display_name():
    #name = "Xuecheng Cai"   #Local scope (available only inside this function)
    #print(name)

#print(name)





#Args = parameters that will pack all arguments into a tuple
#Useful so that a function can accept a varying amount of arguments

#def add(*stuff):
    #sum = 0
    #stuff = list(stuff)
    #stuff[0] = 0
    #for i in stuff:
        #sum += i
    #return sum

#print(add(1,2,3,4,5,6))





#Kwargs = parameters that will pack all arguments into a dictionary
#Useful so that a function can accept a varying amount of keyword arguments

#def hello(**Names):
    #print("Hello " + Kwargs['first'] + " " + Kwargs['last'])
    #print("Hello", end = " ")
    #for key, value in Names.items():
        #print(value, end = " ")

#hello(first = "Xuecheng", middle = "lol", last = "Cai")





#str.format() = optional method that gives users more control when displaying output

#animal = "cow"
#item = "moon"

#print("The " + animal + " jumped over the " + item)

#print("The {} jumped over the {}".format(animal, item))
#print("The {0} jumped over the {1}".format(animal, item)) #positional argument
#print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) #keyword argument

#text = "The {} jumped over the {}"
#print(text.format(animal, item))

#name = "Xuecheng"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. Nice to meet you!".format(name))

#number = 1000

#print("The number is {:,.3f}".format(number))
#print("The number is {:,}".format(number))
#print("The number is {:b}".format(number))
#print("The number is {:o}".format(number))
#print("The number is {:x}".format(number))
#print("The number is {:e}".format(number))





#Random module

#import random

#x = random.randint(1,6)
#y = random.random()

#myList = ["Rock", "Paper", "Scissors"]
#z = random.choice(myList)

#cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

#random.shuffle(cards)

#print(z)





#Exception = events detected during execution that interrupt the flow of a program

#try:
    #numerator = int(input("Enter a number to divide: "))
    #denominator = int(input("Enter a number to divide by: "))
    #result = numerator/denominator

#except ZeroDivisionError as e:
    #print(e)
    #print("You can't divide by zero! Idiot!")

#except ValueError as e:
    #print(e)
    #print("Only integers please!")

#except Exception as e:
    #print(e)
    #print("something went wrong :(")
#else:
    #print(result)
#finally:
    #print("This will always execute")

#import os

#path = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\.vscode"

#if os.path.exists(path):
    #print("This location exists!")
    #if os.path.isfile(path):
        #print("That is a file.")
    #elif os.path.isdir(path):
        #print("That is a directory.")
#else:
    #print("That location doesn't exist!")
#try:
    #with open("test.tx") as file:
        #print(file.read())
#except FileNotFoundError:
    #print("This file was not found :(")

#text = "This file was overwritten!"

#with open('test.txt', 'a') as file:
    #file.write(text)

#copyfile() = copies contents of a file
#copy() = Copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

#import shutil

#shutil.copyfile('test.txt', 'copy.txt') #src,dst

#Moving files

#import os

#source = 'folder'
#destination = 'C:\\Users\\xuech\\Desktop\\folder'

#try:
    #if os.path.exists(destination):
        #print("There is already a file there!")
    #else:
        #os.replace(source,destination)
        #print(source + " was replaced")
#except FileNotFoundError:
    #print(source + " was not found!")

#import os
#import shutil

#path = 'full folder'

#try:
    #os.remove(path)        #delete a file
    #os.rmdir(path)         #delete an EMPTY directory
    #shutil.rmtree(path)     #delete a directory containing files
    #print("File removed!")
#except FileNotFoundError:
    #print("That file was not found!")
#except PermissionError:
    #print("You do not have permission to delete that folder!")
#except OSError:
    #print("You cannot delete this folder containing files with that function.")
#else:
    #print(path + " was deleted!")





#Modules = a file containing python code. May contain functions, classes, etc.
#Used with modular programming, which is to separate a program into useful different parts

#import messages as msg
#from messages import hello, bye

#msg.hello()
#msg.bye()

#help("modules")





#Python Object Oriented Programming, creating real life objects

#from Car import Car

#car_1 = Car("Chevy", "Corvette", "2021", "Blue")
#car_2 = Car("Volkswagen", "USV", "2023", "Black")

#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_2.colour)

#print(car_1.wheels)
#print(car_1.rims)
#print(car_1.spoiler)

#Car.wheels = 2

#print(car_2.wheels)
#print(car_2.rims)
#print(car_2.spoiler)

#car_2.drive()
#car_2.stop()

#Class variables

#car_1 = Car("Chevy", "Corvette", "2021", "Blue")
#car_2 = Car("Volkswagen", "USV", "2023", "Black")


#Inheritance

#class Animal:

    #alive = True
    
    #def eat(self):
        #print("This animal is eating")
    
    #def sleep(self):
        #print("This animal is sleeping")

#class Rabbit(Animal):
    #def run(self):
        #print("This rabbit is running")

#class Fish(Animal):
    #def swim(self):
        #print("This fish is swimming")

#class Hawk(Animal):
    #def fly(self):
        #print("This hawk is flying")

#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

#rabbit.run()
#fish.swim()
#hawk.fly()

#multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

#class Animal(Organism):

    #def eat(self):
        #print("This animal is eating")

#class Dog(Animal):

    #def bark(self):
        #print("This dog is barking")

#dog = Dog()
#print(dog.alive)
#dog.eat()
#dog.bark()
    
#multiple inheritance = when a child class is derived from more than one parent class

#class Prey:

    #def flee(self):
        #print("The animal flees.")

#class Predator:
    
    #def hunt(self):
        #print("This animal hunts.")


#class Rabbit(Prey):
    #pass

#class Hawk(Predator):
    #pass

#class Fish(Prey, Predator):
    #pass


#rabbit = Rabbit()
#hawk = Hawk()
#fish = Fish()

#rabbit.flee()
#hawk.hunt()
#fish.flee()
#fish.hunt()

#Method overriding

#class Animal:

    #def eat(self):
        #print("This animal is eating.")

#class Rabbit(Animal):
    
    #def eat(self):
        #print("The rabbit eat carrots.")

#rabbit = Rabbit()
#rabbit.eat()


#Method chaining
    
#class Car:

    #def turn_on(self):
        #print("You start the engine.")
        #return self
    
    #def drive(self):
        #print("You drive the car.")
        #return self
    
    #def brake(self):
        #print("You step on the brakes.")
        #return self
    
    #def turn_off(self):
        #print("You turn off the engine.")
        #return self
    
#car = Car()

#car.turn_on().drive()

#car.brake().turn_off()

#car.turn_on()\
    #.drive()\
    #.brake()\
    #.turn_off()





#super() = Function used to give access to the methods of a parent class.
#          Returns a temporary object of a parent class when used.
    
#class Rectangle:
    #def __init__(self, length, width):
        #self.length = length
        #self.width = width

#class Square(Rectangle):

    #def __init__(self, length, width):
        #super().__init__(length, width)

    #def area(self):
        #return self.length * self.width

#class Cube(Rectangle):

    #def __init__(self, length, width, height):
        #super().__init__(length, width)
        #self.height = height

    #def volume(self):
        #return self.length * self.width * self.height

#square = Square(3, 3)
#cube = Cube(3, 3, 3)

#print(square.area())
#print(cube.volume())





#Abstract classes = Prevents a user from creating an object of that class
#Compels a user to override abstract methods in a child class

#Abstract class = a class which contains one or more abstract methods
#Abstract method = a method that has a declaration byt does not have an implementation

#from abc import ABC, abstractmethod    #abc stands for abstract based class

#class Vehicle(ABC):
    
    #@abstractmethod
    #def go(self):
        #pass

    #@abstractmethod
    #def stop(self):
        #pass

#class Car(Vehicle):

    #def go(self):
        #print("You drive the car.")
    
    #def stop(self):
        #print("This car is stopped.")

#class Motorcycle(Vehicle):

    #def go(self):
        #print("You ride the motorcycle.")

    #def stop(self):
        #print("This motorcycle is stopped.")
    
#vehicle = Vehicle()
#car = Car()
#motorcycle = Motorcycle()

#car.go()
#motorcycle.go()

#car.stop()
#motorcycle.stop()

#class Car:

    #colour = None

#class Motorcycle:

    #colour = None

#def change_colour(car, colour):
    #car.colour = colour

#car_1 = Car()
#car_2 = Car()
#car_3 = Car()

#bike_1 = Motorcycle()

#change_colour(car_1, "red")
#change_colour(car_2, "green")
#change_colour(car_3, "blue")
#change_colour(bike_1, "black")

#print(car_1.colour)
#print(car_2.colour)
#print(car_3.colour)
#print(bike_1.colour)





#Duck typing = a concept where the class of an object is less important that the methods/attributes
#class tyep is not checked if minimum methods methods/attributes are present
#"If it walks like a duck, and it quacks like a duck, then it must be a duck."

#class Duck:

    #def walk(self):
        #print("This duck is walking.")

    #def talk(self):
        #print("This duck is quacking.")

#class Chicken:

    #def walk(self):
        #print("This chicken is walking.")

    #def talk(self):
        #print("This chicken is clucking.")

#class Person:

    #def catch(self, duck):
        #duck.walk()
        #duck.talk()
        #print("You caught the critter!")

#duck = Duck()
#chicken = Chicken()
#person = Person()

#person.catch(chicken)





#walrus operator :=

#new to python 3.8
#aka assignment expression
#assigns values to variables as part of a larger expression

#foods = list()

#while True:
    #food = input("What food do you like?: ")
    #if food == "quit":
        #break
    #foods.append(food)

#foods = list()

#while food := input("What food do you like?: ") != "quit":
    #foods.append(food)





#Assigning function to a variable

#def hello():
    #print("Hello")

#hi = hello
#hello()
#hi()

#say = print
#say("Whoa! I can't believe this works! :O")

#Higher Order Functions = A function that either:
                        #1. accepts a function as an argument, or
                        #2 returns a function (In python, functions are also treated as objects)
    
#def divisor(x):
    #def dividend(y):
        #return y/x
    #return dividend

#divide = divisor(2)
#print(divide(10))
    





#Lambda function = Function written in 1 line using lambda keyword
                    #Accepts any number of arguments, but only has one expression. (Think of it as a shortcut)
                    #(Useful if needed for a short period of time, throw-away)

#lambda parameters:expression

#def double(x):
    #return x * 2
#print(double(5))   

#double = lambda x:x*2
#multiply = lambda x, y: x*y

#add = lambda x, y, z: x + y + z
#full_name = lambda first_name, last_name: first_name + " " + last_name
#check_age = lambda age:True if age >= 18 else False

#print(check_age(18))
#print(full_name("Xuecheng", "Cai"))
#print(add(5,6,7))

#sort() method = used with lists
#sort() function = used with iterables

#students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

#students.sort(reverse = True)
#sorted_students = sorted(students, reverse=True)

#for i in sorted_students:
    #print(i)

#students = (("Squidward", "F", 60),
            #("Sandy", "A", 33),
            #("Patrick", "D", 36),
            #("Spongebob", "B", 20),
            #("Mr.Krabs", "C", 78))
            
#age = lambda ages: ages[2]

#students.sort(key = age)

#sorted_students = sorted(students, key = age)

#for i in sorted_students:
    #print(i)





#map() = applies a function to each item in an iterable (list, tuple, etc.)
#map(function, iterable)
    
#store = [("shirt", 20.00),
         #("pants", 25.00),
         #("jacket", 50.00),
         #("socks", 10.00)]

#to_euros = lambda data: (data[0], data[1] * 0.82)
#to_dollars= lambda data: (data[0], data[1] / 0.82)

#store_dollars = list(map(to_dollars, store))

#for i in store_dollars:
    #print(i)





#filter() = creates a collection of elements from an iterable for which a function returns
#filter(function, iterable)

#friends = [("Rachel", 19),
           #("Monica", 18),
           #("Phoebe", 17),
           #("Joey", 16),
           #("Chandler", 21),
           #("Ross", 20)]

#age = lambda list: list[1] >= 18

#party_buds = list(filter(age, friends))

#for i in party_buds:
    #print(i)

#reduce() = apple a function to an interable and reduces it to a single cumulative value.
            #performs function on first two elements and repeats process until 1 value remains 
    
    #reduce(function, iterable)

#import functools

#letters = ["H", "E", "L", "L", "O"]
#word = functools.reduce(lambda x, y : x + y, letters)
#print(word)

#factorial = [5,4,3,2,1]
#result = functools.reduce(lambda x, y: x * y, factorial)
#print(result)





#list comprehension = a way to create a new list with less syntax
                    #can mimic certain lambda functions, easier to read
                    #list = [expression (if/else) for item in iterable]

#squares = []                #create an empty list
#for i in range(1,11):       #create a for loop
    #squares.append(i * i)   #define what each loop iteration should do

#print(squares)

#squares = [i * i for i in range (1,11)]

#print(squares)

#students = [100,90,80,70,60,50,40,30,0]

#passed_students = list(filter(lambda x: x > 50, students))

#passed_students = [i for i in students if i > 50]

#passed_students = [i if i  > 50 else "FAILED" for i in students]

#print(passed_students)





#dictionary comprehension = create dictionaries using an expression
                            #can replace for loops and certain lambda functions
                            #dictionary = {key: expression for (key,value) in iterable}

#cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

#cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}

#print(cities_in_C)

#weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}

#sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
#print(sunny_weather)

#cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities_in_F.items()}

#print(desc_cities)

#def check_temp(value):
    #if value >= 70:
        #return "HOT"
    #elif 69 >= value >= 40:
        #return "WARM"
    #else:
        #return "COLD"

#cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#desc_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}

#print(desc_cities)





#zip(*iterables) = aggregate elemtns from two or more iterables (list, tuples, sets, etc.)
                    #creates a zip object with paired elements sotred in tuples for each element

#usernames = ["ZPGStudios", "Australianping", "YoWassup"]    #list
#passwords = ("6123", "12345", "Password")                   #tuple
#login_date = ["1/1/2024", '1/2/2023', "1/3/2022"]

#users_login = zip(usernames, passwords, login_date)
#users = dict(zip(usernames, passwords))                           #zip

#for i in users_login:
    #print(i)

#for key, value in users.items():
    #print(key + ": " + value)

#print(type(users_login))





#if __name__ = "__main__"
#Python interpreter sets "special variables", one of which is __name__
#Python will assign the __name__ variable a value of "__main__" if it's the initial module being run

#def main():
    #print("Hello!")

#if __name__ == "__main__":
    #main()





#time module

#import time

#print(time.ctime(0))        #convert a time expressed in seconds since epoch to a readable string
#print(time.time())          #return current seconds since epoch

#print(time.ctime(time.time()))

#time_object = time.localtime()
#time_object = time.gmtime()
#print(time_object)
#local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)

#time_string = "12 January, 2024"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)

#time_tuple = (2024, 1, 12, 7, 59, 52, 5, 0, 0)
#time_string = time.asctime(time_tuple)
#print(time_string)





#multi-threading = a flow of execution. Like a separate order of instructions.
                    #However each thread takes a turn running to achieve concurrency.
                    #GIL = Global Interpreter Lock, allows only one thread to hold the control of the Python interpreter

#CPU bound = program/task spends most of its time waiting for internal events (CPU intensive)
            #use multiprocessing

#io bound = program/task spends most of its time waiting for external events (user inputs, web scraping)
            #use multithreading

#import threading
#import time

#def eat_breakfast():
    #time.sleep(3)
    #print("You ate breakfast")

#def drink():
    #time.sleep(4)
    #print("You drank water")

#def study():
    #time.sleep(5)
    #print("You finished your homework")

#x = threading.Thread(target = eat_breakfast, args = ())
#x.start()

#y = threading.Thread(target = drink, args = ())
#y.start()

#z = threading.Thread(target = study, args = ())
#z.start()

#x.join()
#y.join()
#z.join()

#eat_breakfast()
#drink()
#study()

#print(threading.active_count())
#print(threading.enumerate())
#print(time.perf_counter())





#daemon threading = a thread that runs in the background, not important for program to run your program will not wait for daemon threads to complete before exiting
#unlike non-daemon threads that cannot normally be killed, stay alike until task is complete

#eg. background tasks, garbage collection, waiting for input, long running processes

#import threading
#import time

#def timer():
    #print()
    #count = 0
    #while True:
        #time.sleep(1)
        #count += 1
        #print("logged in for: ", count, " seconds")

#x = threading.Thread(target= timer, daemon = True)
#x.start()

#print(x.isDaemon())

#answer = input("Do you wish to exit?")





#multi-processing = runnning tasks in parallel on different cpu cores, bypasses GIL used for threading
                    #multiprocessing is better for cpu bound tasks (heavy cpu usage)
                    #multithreading is better for io bound tasks (waiting around)

#from multiprocessing import Process, cpu_count
#import time

#def counter(num):
    #count = 0
    #while count < num:
        #count += 1

#def main():

    #print(cpu_count())

    #a = Process(target=counter, args=(125000000,))
    #b = Process(target=counter, args=(125000000,))
    #c = Process(target=counter, args=(125000000,))
    #d = Process(target=counter, args=(125000000,))
    #e = Process(target=counter, args=(125000000,))
    #f = Process(target=counter, args=(125000000,))
    #g = Process(target=counter, args=(125000000,))
    #h = Process(target=counter, args=(125000000,))
    
    #a.start()
    #b.start()
    #c.start()
    #d.start()
    #e.start()
    #f.start()
    #g.start()
    #h.start()

    #a.join()
    #b.join()
    #c.join()
    #d.join()
    #e.join()
    #f.join()
    #g.join()
    #h.join()

    #print("Finished in: ", time.perf_counter() , "seconds")


#if __name__ == '__main__':
    #main()





#GUI = Graphical user Interface

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets

#from tkinter import *
#import os

#window = Tk()       #instantiate an instance of a window
#window.geometry("420x420")
#window.title("Xuecheng's First GUI")

#file_path = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Stickman.png"

#print(os.access(file_path, os.R_OK))

#icon = PhotoImage(file= file_path)
#window.iconphoto(True,icon)

#window.config(background="#4287f5")

#window.mainloop()   #places window on computer screen, listens for events





#Label = an area widget that holds text and/or an image within a window

#from tkinter import *

#window = Tk()

#photo = PhotoImage(file="C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Stickman.png")


#label = Label(window, 
              #text="ayo what's good", 
              #font = ("comic sans", 40, "bold"), 
              #fg = ("#4287f5"), 
              #bg = "Black",
              #relief = RAISED,
              #bd = 10,
              #padx = 20,
              #pady = 20,
              #image = photo,
              #compound = "top")

#label.pack()
#label.place(x = 0, y = 0)

#window.mainloop()





#button = you click it, then it does stuff

#from tkinter import *

#count = 0

#def click():
    #global count
    #count += 1
    #print(count) 

    #print("You clicked the button!")

#window = Tk()

#photo = PhotoImage(file="C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Stickman.png")

#button = Button(window,
                #text = "Click me!",
                #command = click,
                #font = ("Comic Sans", 30),
                #fg = "#4287f5",
                #bg = "black",
                #activeforeground="#4287f5",
                #activebackground= "black",
                #state = ACTIVE,
                #mage = photo,
                #compound = "bottom")
#button.pack()

#window.mainloop()





#entry widget = a textboxt that accepts a single line of user input

#from tkinter import *

#def submit():
    #username = entry.get()
    #print("Hello " + username)
    #entry.config(state=DISABLED)

#def delete():
    #entry.delete(0, END)

#def backspace():
    #entry.delete(len(entry.get()) - 1, END)

#window = Tk()

#entry = Entry(window,
              #font = ("Comic Sans", 50),
              #fg = "#4287f5",
              #bg= "BLACK",
              #show = "*")

#entry.insert(0, "Spongebob")
#entry.pack(side=LEFT)

#submit_button = Button(window, text = "Submit", command = submit)
#submit_button.pack(side=RIGHT)

#delete_button = Button(window, text = "Delete", command = delete)
#delete_button.pack(side=RIGHT)

#backspace_button = Button(window, text = "Backspace", command = backspace)
#backspace_button.pack(side=RIGHT)

#window.mainloop()





#check boxes

#from tkinter import*

#def display():
    #if(x.get() == 1):
        #print("You agree to Stickman")
    #else:
        #print("You don't agree to Stickman")

#window = Tk()

#x = IntVar()

#photo = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Stickman.png")

#check_button = Checkbutton(window,
                           #text = "I agree to Stickman",
                           #variable = x,
                           #onvalue=1,
                           #offvalue=0,
                           #command=display,
                           #font = ("Comic Sans", 20),
                           #fg = "#4287f5",
                           #bg="Black",
                           #activeforeground="#4287f5",
                           #activebackground="Black",
                           #padx=25,
                           #pady=10,
                           #image = photo,
                           #compound = LEFT)

#check_button.pack()

#window.mainloop()
    




    #radio button = similar to checkbox, but you can only select one from a group

#from tkinter import *

#def order():
    #if(x.get()) == 0:
        #print("You ordered Pizza!")
    #elif(x.get()) == 1:
        #print("You ordered a Hamburger!")
    #elif(x.get()) == 2:
        #print("You ordered a hotdog!")
    #else:
        #print("Huh?")

#food = ["Pizza", "Hamburger", "Hotdog"]

#window = Tk()

#pizzaImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Pizza.png")
#hamburgerImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Hamburger.png")
#hotdogImage = PhotoImage (file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Hotdog.png")

#foodImages = [pizzaImage, hamburgerImage, hotdogImage]

#x = IntVar()

#for index in range(len(food)):
    #radiobutton = Radiobutton(window, 
                              #text = food[index],       #adds text to radiobuttons
                              #variable = x,             #groups radiobuttons together if they share the same variable
                              #value = index,            #assigns each radiobutton a different value
                            #padx = 25,                  # adds padding on x-axis
                            #font = ("Impact", 40),
                            #image = foodImages[index],
                            #compound = "left",          #adds image to the left of the text
                            #indicatoron = 0,
                            #width = 800,
                            #command = order             #set command of radiobutton to order() function
                            #)
    
    #radiobutton.pack()

#window.mainloop()\





#Scale

#from tkinter import *

#def submit():
    #if scale.get() == 0:
        #print("It is freezing!")
    #elif scale.get() == 100:
        #print("It is boiling!")
    #else:
        #print("The temperature is: " + str(scale.get()) + " degrees C.")

#window = Tk()

#otImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Hamburger.png")
#hotImage = hotImage.subsample(4,4)
#hotLabel = Label(image = hotImage)

#coldImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Stickman.png")
#coldImage = coldImage.subsample(4,4)
#coldLabel = Label(image=coldImage, compound="bottom")

#scale = Scale(window, from_ = 100, to=0,
#              length=600,
#              orient=VERTICAL,
#              font = ("Comic Sans", 20),
#              tickinterval = 10, #adds a scale indicator
#              showvalue=0, #hides current value
#              troughcolor = "#4287f5",
#              fg="white",
#              bg= "black",
#              activebackground="red",
#              )

#scale.set(((scale['from'] - scale ['to']) / 2) + scale['to'])

#button = Button(window, text = "Submit", command = submit)

#hotLabel.pack()
#scale.pack()
#coldLabel.pack()
#button.pack()


#window.mainloop()





#list box = A listing of selectable text items within its own container


#from tkinter import *

#def submit():
    
    #food = []

    #for index in listbox.curselection():
        #food.insert(index, listbox.get(index))

    #print("You have ordered: ")

    #for index in food:
        #print(index)
    

#def add():

    #new_item = entryBox.get().strip()

    #if new_item and new_item not in listbox.get(0, END):
        #listbox.insert(END, new_item)
        #listbox.config(height = listbox.size())
    #else:
        #print("Item already exists or entry is empty")

#'def delete():

    #for index in reversed(listbox.curselection()):
        #listbox.delete(index)

    #listbox.config(height = listbox.size())

#window = Tk()

#listbox = Listbox(window,
                  #bg = "#f7ffde",
                  #font = ("Constancia", 35),
                  #width = 12,
                  #selectmode = MULTIPLE)

#listbox.pack()

#listbox.insert(1, "Pizza")
#listbox.insert(2, "Pasta")
#listbox.insert(3, "Garlic Bread")
#listbox.insert(4, "Soup")
#listbox.insert(5, "Salad")

#listbox.config(height = listbox.size())

#entryBox = Entry(window)
#entryBox.pack()

#submitButton = Button(window, text = "Submit", command = submit)
#submitButton.pack()

#addButton = Button(window, text = "Add", command = add)
#addButton.pack()

#deleteButton = Button(window, text = "Delete", command = delete)
#deleteButton.pack()

#window.mainloop()





#message boxes

#from tkinter import *
#from tkinter import messagebox          #imports message library

#def click():
    #messagebox.showinfo(title = "This is an info message box", message = "Hello World")
    #while(True):
        #messagebox.showwarning(title = "WARNING", message = "You have a virus!")
    #messagebox.showerror(title = "ERROR", message = "Something went wrong :C")

    #if messagebox.askokcancel(title = "ask ok cancel", message = "Do you want to do the thing"):
        #print("You did a thing!")
    #else:
        #print("You cancelled a thing!")
    #if messagebox.askretrycancel(title = "ask retry cancel", message = "Do you want to retry the thing"):
        #print("You retried a thing!")
    #else:
        #print("You cancelled a thing!")

    #if messagebox.askyesno(title = "ask yes or no", message = "Do you like cake?"):
        #print("I like cake too :)")
    #else:
        #print("Yikes")
    #answer = messagebox.askquestion(title = "Ask question", message = "Do you like pie?")
    #if answer == "yes":
        #print("I like pie too")
    #else:
        #print("yikes")
    
    #answer = messagebox.askyesnocancel(title = "Ask yes no cancel", message = "Do you like to code?", icon = "info")
    #if answer == True:
        #print("You like to code :)")
    #elif answer == False:
        #print("Then why are you here?")
    #else:
        #print("Why are you dodging the question?")

#window = Tk()

#button = Button(window, command = click, text = "Click me")
#button.pack()

#window.mainloop()





#Colour choooser

#from tkinter import *
#from tkinter import colorchooser            #A sub-module

#def click():
    #color = colorchooser.askcolor()
    #colorHex = color[1]
    #print(colorHex)

    #window.config(bg = color[1])


#window = Tk()
#window.geometry("420x420")

#button = Button(text = "Click me", command = click)
#button.pack()

#window.mainloop()





#text widget = functions like a text area, you can enter multiple lines of text

#from tkinter import *

#def submit():
    #input = text.get("1.0", END)
    #print(input)

#window = Tk()

#text = Text(window,
            #bg = "light yellow",
            #font = ("Ink Free", 20),
            #height = 8,
            #width=20,
            #padx = 20,
            #pady = 20,
            #fg = "red")
#text.pack()

#button = Button(window, text = "Submit", command = submit)
#button.pack()

#window.mainloop()





#Opening file (file dialog)

#from tkinter import *
#from tkinter import filedialog

#def openFile():
    #filepath = filedialog.askopenfilename(initialdir = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes",
                                          #title = "Open file",
                                          #filetypes = (("text files", "*txt"),
                                          #("all files", "*.*")))
    #file = open(filepath, "r")
    #print(file.read())
    #file.close()

#window = Tk()

#button = Button(text = "Open", command = openFile)
#button.pack()

#window.mainloop()





#File saving

#from tkinter import *
#from tkinter import filedialog

#def saveFile():
#    file = filedialog.asksaveasfile(initialdir="C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes",
#                                    defaultextension=".txt",
#                                    filetypes=[
#                                        ("Text file", ".txt"),
#                                        ("HTML file", ".html"),
#                                        ("All files", ".*")
#                                    ])

    #filetext = str(text.get(1.0, END))

    #if file is None:                                #prevents exception
        #return
    #filetext = input("Enter some text:")            #using the console window instead
    #file.write(filetext)
    #file.close()
    
#window = Tk()

#button = Button(text = "Save", command = saveFile)
#button.pack()

#text = Text(window)
#text.pack()

#window.mainloop()





#Menu bar

#from tkinter import *

#def openFile():
    #print("File has been opened")

#def saveFile():
    #print("File has been saved")

#def cut():
    #print("You cut some text")

#def copy():
    #print("You copied some text")

#def paste():
    #print("You pasted some text")

#window = Tk()
#window.geometry("420x420")

#openImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Floppy Disk.png")
#openImage = openImage.subsample(50, 50)
#saveImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Open File.png")
#saveImage = saveImage.subsample(12, 12)
#exitImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Exit.png")
#exitImage = exitImage.subsample(10, 10)

#menubar = Menu(window)
#window.config(menu = menubar)

#fileMenu = Menu(menubar, tearoff = 0, font = ("MV Boli", 15))                          #tearoff gets rid of the dotted line
#menubar.add_cascade(label = "File", menu = fileMenu)

#fileMenu.add_command(label = "Open", command = openFile, image = openImage, compound = "left")                          #adds a clickable option to the File menu
#fileMenu.add_command(label = "Save", command = saveFile, image = saveImage, compound = "left")
#fileMenu.add_separator()                                                            #adds a line separator
#fileMenu.add_command(label = "Exit", command = quit, image = exitImage, compound = "left")

#editMenu = Menu(menubar, tearoff = 0, font = ("MV Boli", 15))
#menubar.add_cascade(label = "Edit", menu = editMenu)

#editMenu.add_command(label = "Cut", command = cut) 
#editMenu.add_command(label = "Copy", command = copy)
#editMenu.add_command(label = "Paste", command = paste)  

#window.mainloop()





#Frame = a rectngular container to gruop and hold widgets

#from tkinter import *

#window = Tk()

#frame = Frame(window, bg = "light blue", bd = 5, relief=RAISED)
#frame.place(x=100,y=100)

#Button(frame, text = "W", font = ("Consolas", 25), width = 3).pack(side = TOP)

#Button(frame, text = "A", font = ("Consolas", 25), width = 3).pack(side = LEFT)

#Button(frame, text = "S", font = ("Consolas", 25), width = 3).pack(side = LEFT)

#Button(frame, text = "D", font = ("Consolas", 25), width = 3).pack(side = LEFT)

#window.mainloop()





#Creating multiple windows

#from tkinter import *

#def create_window():
    #new_window = Tk()             #new window "on top" of other windows, linked to a "bottom" window

    #old_window.destroy()            #closes out of the old window

#old_window = Tk()                           #new independent window

#Button(old_window, text = "create new window", command = create_window).pack()

#old_window.mainloop()





#Creating separate tabs

#from tkinter import *
#from tkinter import ttk

#window = Tk()

#notebook = ttk.Notebook(window)             #widget that manages a collection of windows/displays

#tab1 = Frame(notebook)                      #new frame for tab 1
#tab2 = Frame(notebook)                      #new frame for tab 2

#notebook.add(tab1, text = "Tab 1")
#notebook.add(tab2, text = "Tab 2")
#notebook.pack(expand = True,                #expand = expand to fill any space not otherwise used
               #fill = "both")               #fill = fill space on x and y axis

#Label(tab1, text = "Hello, this is Tab #1", width = 50, height = 25).pack()
#Label(tab2, text = "Hello, this is Tab #2", width = 50, height = 25).pack()

#window.mainloop()





#grid() = geometry manager that organizes widgets in a table-like structure in a parent

#from tkinter import *

#window = Tk()

#titleLabel = Label(window, text = "Enter your info", font = ("Arial", 25)).grid(row = 0, column = 0, columnspan = 2)

#firstNameLabel = Label(window, text = "First name: ", width = 20, bg = "red").grid(row = 1, column = 0)
#firstNameEntry = Entry(window).grid(row = 1, column = 1)

#lastNameLabel = Label(window, text = "Last name: ", bg = "green").grid(row = 2, column = 0)
#lastNameEntry = Entry(window).grid(row = 2, column = 1)

#emailLabel = Label(window, text = "Email: ", bg = "blue", width=30).grid(row = 3, column = 0)
#emailEntry = Entry(window).grid(row = 3, column = 1)

#submitButton = Button(window, text = "Submit").grid(row = 4, column = 0, columnspan = 2)


#window.mainloop()





#Progress bar

#from tkinter import *
#from tkinter.ttk import *
#import time

#def start():
    #GB = 100
    #download = 0
    #speed = 1
    
    #while (download < GB):
        #time.sleep(0.05)
        #bar["value"] += ((speed/GB) * 100)
        #download += speed
        #percent.set(str(int((download/GB) * 100)) + "%")
        #text.set(str(download) + "/" + str(GB) + " GB completed")

        #window.update_idletasks()

#window = Tk()

#percent = StringVar()

#text = StringVar()

#bar = Progressbar(window, orient = HORIZONTAL, length = 300)
#bar.pack(pady = 10)

#percentLabel = Label(window, textvariable = percent).pack()

#taskLabel = Label(window, textvariable = text).pack()

#button = Button(window, text = "Download", command = start).pack()

#window.mainloop()





#Canvas = widget that is used to draw graphs, plots, images in a window

#from tkinter import *

#window = Tk()

#canvas = Canvas(window, height = 500, width = 500)
#canvas.create_line(0,0, 500, 500, fill = "Blue", width = 5)
#canvas.create_line(0,500, 500, 0, fill = "Red", width = 5)
#canvas.create_rectangle(50, 50, 250, 250, fill = "Purple")
#points = [250, 0, 500, 500, 0, 500]
#canvas.create_polygon(points, fill = "Green", outline = "Black", width = 5)
#canvas.create_arc(0,0,500,500, style = PIESLICE, start = 270, extent = 180)
#canvas.create_arc(0,0,500,500, fill = "Red", extent = 180, width = 10)
#canvas.create_arc(0,0,500,500, fill = "White", extent = 180, start = 180, width = 10)
#canvas.create_oval(190, 190, 310, 310, fill = "White", width = 10)

#canvas.pack()

#window.mainloop()





#key events

#from tkinter import *

#def doSomething(event):
    #print("You pressed: " + event.keysym)
    #label.config(text=event.keysym)

#window = Tk()

#window.bind("<Key >", doSomething)

#label = Label(window, font= ("Helvetica", 100))
#label.pack()

#window.mainloop()





#mouse events

#from tkinter import *

#def doSomething(event):
    #print("Mouse coordinates: " + str(event.x) + "," + str(event.y))

#window = Tk()

#window.bind("<Button-1>", doSomething)             #Left mouse click
#window.bind("<Button-2>", doSomething)             #Scroll wheel click
#window.bind("<Button-3>", doSomething)             #Right mouse click
#window.bind("<ButtonRelease>", doSomething)        #Any button release
#window.bind("<Enter>", doSomething)                #Enter the window
#window.bind("<Leave>", doSomething)                #Leave the window
#window.bind("<Motion>", doSomething)                #Where the mouse moved

#window.mainloop(),





#Drag and drop

#from tkinter import *

#def drag_start(event):
    #widget = event.widget
    #widget.startX = event.x
    #widget.startY = event.y

#def drag_motion(event):
    #widget = event.widget
    #x = widget.winfo_x() - widget.startX + event.x
    #y = widget.winfo_y() - widget.startY + event.y
    #widget.place(x = x, y = y)

#window = Tk()

#label = Label(window, bg = 'Red', width = 10, height = 5)
#label.place(x = 0, y = 0)

#label2 = Label(window, bg = 'Blue', width = 10, height = 5)
#label2.place(x = 100, y = 100)

#label.bind("<Button-1>", drag_start)
#label.bind("<B1-Motion>", drag_motion)

#label2.bind("<Button-1>", drag_start)
#label2.bind("<B1-Motion>", drag_motion)

#window.mainloop()





#Moving an image on a window

#from tkinter import *

#def move_up(event):
    #label.place(x = label.winfo_x(), y = label.winfo_y() - 10)

#def move_left(event):
    #label.place(x = label.winfo_x() - 10, y = label.winfo_y())

#def move_down(event):
    #label.place(x = label.winfo_x(), y = label.winfo_y() + 10)

#def move_right(event):
    #label.place(x = label.winfo_x() + 10, y = label.winfo_y())

#window = Tk()
#window.geometry("500x500")

#window.bind("<w>", move_up)
#window.bind("<a>", move_left)
#window.bind("<s>", move_down)
#window.bind("<d>", move_right)

#window.bind("<Up>", move_up)
#window.bind("<Left>", move_left)
#window.bind("<Down>", move_down)
#window.bind("<Right>", move_right)

#myimage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Racecar.png")
#myimage = myimage.subsample(4,4)
#label = Label(window, image = myimage, bg = "red")
#label.place(x = 0, y = 0)

#window.mainloop()





#Moving an image on a canvas

#from tkinter import *

#def move_up(event):
    #canvas.move(myimage, 0, -10)
    
#def move_left(event):
    #canvas.move(myimage, -10, 0)

#def move_down(event):
    #canvas.move(myimage, 0, 10)

#def move_right(event):
    #canvas.move(myimage, 10, 0)


#window = Tk()

#window.bind("<w>", move_up)
#window.bind("<a>", move_left)
#window.bind("<s>", move_down)
#window.bind("<d>", move_right)
#window.bind("<Up>", move_up)
#window.bind("<Left>", move_left)
#window.bind("<Down>", move_down)
#window.bind("<Right>", move_right)

#canvas = Canvas(window, width = 500, height = 500)
#canvas.pack()

#photoImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Racecar.png")
#myimage = canvas.create_image(0,0, image = photoImage, anchor = NW)

#window.mainloop()





#2D animations

#from tkinter import *
#import time

#WIDTH = 500
#HEIGHT = 500

#xVELOCITY = 3
#yVELOCITY = 2

#window = Tk()

#canvas = Canvas(window, width = WIDTH, height = HEIGHT)
#canvas.pack()

#background_photo = PhotoImage(file="C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\Space.png")
#background_photo = background_photo.subsample(int(background_photo.width() / WIDTH), int(background_photo.height() / HEIGHT))
#background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

#photoImage = PhotoImage(file = "C:\\Users\\xuech\\Documents\\Programming\\Projects\\Python\\Full Course Notes\\UFO.png")
#myImage = canvas.create_image(0, 0, image = photoImage, anchor = NW)

#image_width = photoImage.width()
#image_height = photoImage.height()

#while True:
#    coordinates = canvas.coords(myImage)
#    print(coordinates)
#
#    if(coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0):
#        xVELOCITY = -xVELOCITY
#    if(coordinates[1] >= (HEIGHT - image_height) or coordinates[0] < 0):
#        yVELOCITY = -yVELOCITY
#
#    canvas.move(myImage, xVELOCITY, yVELOCITY)
#    window.update()
#    time.sleep(0.01)
#
#window.mainloop()





#Multiple animations

#from tkinter import *
#import time
#from Ball import *

#window = Tk()

#WIDTH = 500
#HEIGHT = 500

#canvas = Canvas(window, width = WIDTH, height = HEIGHT)
#canvas.pack()

#volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "White")
#tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "Green")
#basketball = Ball(canvas, 0, 0, 125, 2, 3, "Orange")

#while True:
    #volley_ball.move()
    #tennis_ball.move()
    #basketball.move()
    #window.update()
    #time.sleep(0.01)

#window.mainloop()





#Email

#import smtplib

#sender = "xuechengc2019@gmail.com"
#receiver = "zpgxuecheng@gmail.com"
#password = "ZpgCraft6123_"
#subject = "Python Email"
#body = "Hello World I wrote this email from Python"


#Header
#message = f'''From: Xuecheng {sender}
#To: {receiver}
#Subject: {subject}\n
#{body}
#'''
#server = smtplib.SMTP("smtp.gmail.com", 587)
#server.starttls()

#try:
#    server.login(sender, password)
#    print("Logged in...")
#    server.sendmail(sender, receiver, message)
#    print("Email has been sent!")
#except smtplib.SMTPAuthenticationError:
#    print("Unable to sign in")
#except smtplib.SMTPServerDisconnected:
#    print("An established connection was aborted by the software in your host machine")





#run .py file with cmd

#save file as .py
#go to command prompt
#navigate to directory w/ your file: cd C:\Users\xuech\Documents\Programming\Projects\Python\Full Course Notes
#invoke python interpreter + script: python GUI.py

#print("Hello World!")
#name = input("What's your name? ")

#print("Hello " + name)





#Python pip

#pip = package manager for packages and modules from Python Package Index

#included for Python 3.4+


#testing for loop
#numbers = [1,2,3,4,5]

#for num in range(len(numbers)):
    #print(numbers[num])


#testing f-strings
#name = "Bob"
#age = 45

#sentence = f"My name is {name} and I am {age} years old."
#print(sentence)


#.join() method

#letters = ['a', 'b', 'c', 'd']
#print("".join(letters))
#print("---".join(letters))
