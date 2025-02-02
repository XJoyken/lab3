#Python Functions
#In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")
#To call a function, use the function name followed by parenthesis:
my_function()
#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Arguments are often shortened to "args" in Python documentations.

#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

#The number of arguments called must match the number of arguments given. 
#Otherwise it gives an error

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")


#Arbitrary Arguments, *args

#If we do not know how many arguments that will be passed into our function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Arbitrary Arguments are often shortened to "*args" in Python documentations. 


#Keyword Arguments:
#We can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#The phrase Keyword Arguments are often shortened to "kwargs" in Python documentations.


#Arbitrary Keyword Arguments, **kwargs:
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#Arbitrary Kword Arguments are often shortened to "**kwargs" in Python documentations.

#Default Parameter Value:
#If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument:
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


#Return Values:
#To let a function return a value, use the return statement:\

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#The pass Statement:
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def myfunction():
  pass


#Positional-Only Arguments:
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
#To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)

my_function(3)

#Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
#Otherwise it will give an error
def my_function(x):
  print(x)

my_function(x = 3)

#Keyword-Only Arguments:
#To specify that a function can have only keyword arguments, add *, before the arguments:
#otherwise it will give an error
def my_function(*, x):
  print(x)

my_function(x = 3)


#Combine Positional-Only and Keyword-Only:
#You can combine the two argument types in the same function.
#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


#Recursion:
#Recursion is a common mathematical and programming concept. It means that a function calls itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


#Python Lambda:
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#Syntax
#lambda arguments : expression

#Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:
x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)
print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time.


#Python Classes/Objects
#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a Class:
class MyClass:
  x = 5

#Create Object:
p1 = MyClass()
print(p1.x)


#The __init__() Function:
"""
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#The __init__() function is called automatically every time the class is being used to create a new object.


#The __str__() Function:
#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:
#Without __str__:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)

#With __str__:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)


#Object Methods:
#Objects can also contain methods. Methods in objects are functions that belong to the object.


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

#The self Parameter:
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


#Modify Object Properties:
p1.age = 40


#Delete Object Properties:

#You can delete properties on objects by using the del keyword:
del p1.age


#Delete Objects:
del p1


#The pass Statement:
#class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass


#Python Inheritance:
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""

#Create a Parent Class:
#Any class can be a parent class, so the syntax is the same as creating any other classAny class can be a parent class, so the syntax is the same as creating any other class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#Create a Child Class:
#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("Mike", "Olsen")
x.printname()


#Add the __init__() Function:
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    #Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
    Person.__init__(self, fname, lname)
    #Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.


#Use the super() Function:
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent::

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

#Add Properties:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
#-------
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)


#Add Methods:
#Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.