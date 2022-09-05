# Python Basics 🔤🐥

## 1. Printing to the console 🖥️
`print()` can be used to output any sort of textual data to the terminal. This line of code...
```python
print('Hello World')
```
...will print the words Hello World to the terminal

## 2. Variables $xyz$
Variables are mutable containers for storing and referencing data values.
```python
a = 12
name = 'Saad'
flag = True
```
These containers can be useful when we want to reference the same value in multiple places or change them all.

## 3. Receiving Input ⌨️
`input()` can be used to receive input from the user which they can type into the console. This function always returns a string which can be casted into another type. It can take a string argument which will be printed as a prompt to the user. This line of code...
```python
input('Enter your name: ')
```
...will prompt the user on the termincal to enter their name like this:
```
Enter your name: 
```

## 4. Type Casting ↔️
There are 3 main data types in python:
*	Numeric like `64` or `9.99`
*	Textual like `'a'` or `"HELLO"`
*	Boolean like `True` or `False`
They can be converted between each other in python. For example, an integer can be converted into a string like this:
```python
num = 363
string = str(num)
string
```
```
'363'
```
Or a string can be converted into integer like this:
```python
string = '8989'
num = int(string)
num
```
```
8989
```
Futher information on type casting can be found [here](https://www.w3schools.com/python/python_casting.asp).

## 5. Strings 🔤
Strings are basically text in python. They are enclosed in either single quotation (`'hello'`) or double quotation (`"hello"`). Like all data, strings can be assigned to a variable like `name = "John"`.\
Two string objects can be *concatenated* together using the `+` operator like this:
```python
first_name = 'Saad'
last_name = 'Rasheed'
first_name + last_name
```
```
'SaadRasheed'
```

Strings are basically an array of characters, hence they have all the slicing and indexing capabilities of a list. However, the characters are immutable, i.e they cannot be changed. For example...
```python
string = 'Aaad Rasheed'
string[0] = 'S'
```
...will result in an error.

### Methods
Strings objects have tons of methods that can be used to manipulate them.
* `upper()` converts all alphabetical characters in a string to uppercase.
* `lower()` converts all alphabetical characters in a string to lowercase.
* `find()` takes a sub-string as an argument, finds it within the main string, and returns the index of where that sub-string starts. If it could not find the sub-string within the string, it returns -1.
* `index()` is the same as `find()` but raises an error if the sub-string is not found.
* `replace()` takes two sub-strings as arguments and replaces all occurences of the first sub-string within the main string with the second sub-string.
* for more string methods, visit [here](https://www.w3schools.com/python/python_strings_methods.asp).

## 6. Operators 👨‍⚕️

### Arithmetic Operators ➕➖✖️➗
These are used with numeric values to perform mathematical operations.
* `+` is used to add numbers.
* `-` is used to subtract numbers.
* `*` is used to multiply numbers.
* `%` is used for modulus.
* `**` is used to raise a number to a power.
* `//` is used to divide numbers and then round the result down to nearest integer.

### Assignment Operators
These are used to assign values to containers.
* `=` is simply used to assign a value to a container.
* Rest of the assignment operators perform some operation on variable and assigns the result to itself. For example:
    * `a += 3` would add 3 to `a` and then assign the result to itself.
    * `b /= 2` would divide `b` by 2 and then assign the result to itself.

### Comparision Operators
These operators compare two objects and return a boolean result.
* `==` checks for equality and returns `True` if the objects are same, else returns `False`.
* `>` checks if the first object is greater than the second.
* `<` checks if the first object is lesser than the second.
* `!=` checks for inequality and returns `True` if the objects are different, else returns `False`.
* `<=` returns `True` if the first object is lesser than or equal to the second object, else returns `False`.
* `>=` returns `True` if the first object is greater than or equal to the second object, else returns `False`.

### Logical Operator
These operators are used to combine boolean expressions.
* `and` returns `True` if both expressions are true, else returns `False`.
* `or` returns `True` if atleast one of the expressions is true, else returns `False`.
* * `not` inverts the result of a boolean expression.

### Identity Operators
These operators check to see if the objects are same, i.e have the same memory location.
* `is` returns `True` if both objects are actually the same, else returns `False`.
* `is not` inverts `is`

### Membership Operators
These operators check if a sequence/value/object is within an object.
* `x in y` returns `True` if `x` is a object/sequence/value within `y`.
* `not in` inverts `in`.

## 7. Conditional Statement
`if` statements are used to define control flow of an algorithm. The syntax is as follows:
```python
if expression_1:
    # code to run if expression_1 is true
elif expression_2:
    # code to run if expression_1 is false but expression_2 is true
else:
    # code to run if expression_1 and expression_2 are both false

# code to run regardless of expressions' truth value
```

## 8. Sequences
Sequences are collection of values instead of a single value like in a variable. They are able to store one or more values.

### Lists
A `list` contains ordered, mutable, indexed and duplicatable values. Syntax:
```python
arr = [1, 2.5, 'a', True, 'hello']
```
* Indexing: Lists are indexed so every element is referenceable with a number. For example, `arr[0]` will return `1`, `arr[1]` will return `2.5`, `arr[2]` will return `'a'` and so on. 
* Slicing: Lists can also be sliced, meaning a sub-set of the list can be obtained. `arr[a:b]` will return elements within `arr` stored at index `a` all the way to index `b-1` (`b` is not inclusive). So `arr[1:4]` will return `[2.5, 'a', True]`.

#### Methods
* `append()` takes a value as an argument and appends it at the end of the list.
* `insert()` takes an integer value for the index and a value, and stores the value at the specified index.
* `remove()` takes a value as an argument and removes it from the list.
* `pop()` takes the index position as the argument and removes the value at that index.
* `clear()` removes all elements from a list.
* `reverse()` reverses the order of elements within the list.

### Tuples
A tuple is the same as a list, except that it's elements are immutable. Syntax:
```python
tup = (1, 2.5, 'a', True, 'hello')
```
Indexing on tuples is the same as lists but assignment is not possible with tuples.

#### Methods
* `count()` takes a value as argument and returns the number of times that value occured within the tuple.
* `index()` takes a value as argument and returns the first index at which it occurs within the tuple. Raises an error if the value is not found.

### Sets
A set contains unordered, immutable and unique values. Syntax:
```python
pack = {1, 2.5, 'a', True, 'hello'}
```
Indexing is not possible on sets since the items within them don't have any order. Items themselves are immutable but they can be removed from the set and new values can be added to it.

#### Methods:
* `add()` takes a value as an argument and adds it to the set.
* `remove()` takes a value as an argument and removes it from the set. If the value is not in set, `remove()` will raise an error.
* `discard()` works the same as `remove()` but will not raise an error if the value is not found in set.
* `clear()` clears out the set.
* for more set methods, visit [here](https://www.w3schools.com/python/python_sets_methods.asp).

## 9. Loops ➰
Loops are used to run a set of instructions multiple times. The number of times is decided by type of loop used, expression provided to the loop or number set by the programmer.

### `for` loop
`for` loop is used to iterate over an array (list, string, dictionary or tuple). It works alot like an iterator where it can execute a set of intructions for every element in the array. Syntax:
```python
for x in y:
    # instructions to run
```

### `while` loop
`while` loop is used to run a set of instructions while a condition is true. Syntax:
```python
while expression:
    # instructions to run
```
This could result in an infinitely running loop unless the set of instruction cause the truth value of expression to change.

### Control Statements
Control statements are used to change the control flow of an algorithm.
* `break` is used to break out of a loop unconditionally.
* `continue` is used to stop the current iteration of the loop and start the next one.
* `pass` is usually used as a place-holder for actual code so that python interpreter doesn't give an error.
