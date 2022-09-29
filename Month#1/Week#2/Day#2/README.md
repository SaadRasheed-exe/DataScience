# Loops

## Task
The provided code stub reads and integer, $n$, from STDIN. For all non-negative integers $i < n$, print $i^2$.

## Example
$n = 3$\
The list of non-negative integers that are less than $n = 3$ is `[0, 1, 2]`. Print the square of each number on a separate line.
```
0
1
4
```
## Input Format

The first and only line contains the integer, $n$.

## Constraints

$1 \le n \le 20$

## Output Format

Print $n$ lines, one corresponding to each $i$.

## Sample Input
```
5
```
## Sample Output
```
0
1
4
9
16
```

## Solution
```python
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
```

# Functions
## Background
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.\
In the Gregorian calendar, three conditions are used to identify leap years:
* The year can be evenly divided by 4, is a leap year, unless:
  * The year can be evenly divided by 100, it is NOT a leap year, unless:
    * The year is also evenly divisible by 400. Then it is a leap year.\
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

## Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean `True`, otherwise return `False`.\
Note that the code stub provided reads from STDIN and passes arguments to the `is_leap` function. It is only necessary to complete the `is_leap` function.

## Input Format
Read `year`, the year to test.

## Constraints
$1900 \le year \le 10^6$

## Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.

## Sample Input
```
1990
```
## Sample Output
```
False
```
## Explanation
1990 is not a multiple of 4 hence it's not a leap year.

## Solution
```python
def is_leap(year):
    leap = False
    
    if not year % 400:
        leap = True
    elif not year % 100:
        leap = False
    elif not year % 4:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
```
