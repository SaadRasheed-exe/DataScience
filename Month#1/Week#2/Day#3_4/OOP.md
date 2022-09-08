# Object Oriented Programming with Python

## What is OOP?
Object oriented programming is a paradigm of programming that's widely used since it simplifies alot of the complexities that arised without it.
In functional programming, you only have a limited set of data types (int, float, chars, string or boolean) and these cannot solve real life problems by themselves without making the code complex. Suppose, we need to represent an object (e.g a table) in our code. It can have alot of properties (e.g color, manufacturer, dimensions, price).\
* **Classes** can help to represent an object in code.
* **Objects** are instances/examples of those classes
* **Methods** are operations that you can perform on objects.\

## OOP in Python
Following code define a class for table in python:
```python
class Table:
    def __init__(self, manufacturer, color, price):
        self.manufacturer = manufacturer
        self.color = color
        self.price = price

t1 = Table('Ashley Furniture Industries', 'Brown', 499)
```
* It is a convention to define a class with first letter capital.
* `__init__` is the constructor function which is invoked when we try to instantiate an object of the class.
* `self` is a reference to the object being instantiated.
* `self.manufacturer`, `self.color` and `self.price` are all properties/attributes of the object.

## Built-in Methods and Attributes
These are functions/attributes that are built-in and necessary for any class. We don't define them, but instead we can override some of their functionalities or values. This gives us more flexibility over our classes. These functions/attributes have trailing underscores (__) in the start and end of their name. Some examples of these functions/attributes are:
* `__init__()` is the constructor for the class.
* `__class__` is an attribute of every object that stores the class name.
* `__len__()` is the function that is called when python's built-in function `len()` is called with the object.

## Custom Methods
Similar to real objects, we can perform operations on objects of classes. For this, we can define our own methods. These methods could change or return the attributes of objects or change their state in some way. For example:
```python
class Table:
    .
    .
    .
    
    def change_price(self, new_price):
        self.price = new_price

t1 = Table('Ashley Furniture Industries', 'Brown', 499)
t1.change_price(400)
```
`change_price()` function takes the `new_price` parameter and changes the `price` of an object of `Table` class. The instance `t1` invokes this function and changes the price from 499 to 400.

## Static Methods
These methods are functions that are not attached to the objects of a class but instead to the class itself. They do not take the `self` parameter. For example:
```python
class Table:
    .
    .
    .

    def static_example():
        print('This is a static function.')

t1 = Table('Ashley Furniture Industries', 'Brown', 499)
t1.static_example() # this will give an error
```
```
TypeError: static_example() takes 0 positional arguments but 1 was given
```
All non-static class methods take the reference of the object as the first argument. Whenever we invoke a function with an object, it's reference is passed as the first argument to the function. In the above example, `static_example` function takes no arguments, hence the error.\
To invoke a static function,
```python
Table.static_example()
```
```
This is a static function.
```

## Inheritance
Sometimes when we have multiple objects represented in our code, they can belong to the same set which have some same properties. For example, in an online educational website, a teacher and a student both belong to the set 'user'. Teacher and student may have the same properties, e.g name, age, address. In this case, instead of defining two classes, each with all three properties, a **super class** (user) can be defined from  which the teacher and student class can inherit their common attributes and properties.
```python
class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return  f'{self.name} {self.age} {self.address}'

class Student(User):
    def __init__(self, name, age, address, courses):
        super.__init__(name, age, address)
        self.courses = courses

class Teacher(User):
    def __init__(self, name, age, address, salary):
        super.__init__(name, age, address)
        self.salary = salary
    
    def __str__(self):
        return 'I am a teacher!'

john = Student('John', 17, '23 Wellington St.', ['Data Science with Python', 'Introduction to PowerBI'])
teach = Teacher('Jose', 32, '221B Baker Street', 5000)

print(john)
print(teach)
```
```
John 17 23 Wellington St.
I am a teacher!
```
* To inherit a class, enter its name in parenthesis with the **child class**.
* `super` refers to the instance's part of super class.
* Functions defined in super class can be overridden in child classes.
