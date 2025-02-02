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