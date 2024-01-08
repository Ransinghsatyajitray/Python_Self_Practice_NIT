"""
Python is one of the General Purpose, 
High level(like English),
Object oriented and 
Interpreted programming language

1. Simple and Esy to Learn : rich set of modules, module is a collection of function
2. Dynamically Programming Lang : we dont need to mention the data type (C, CPP, Java are static programming language)
3. Platform Independent Lang
4. Portable
5. Interpreted Programming Lng
6. High Level Programming Lng
7. Procedural(Functional) and OOP Lang'
8. Robust
9. Extensible 
10. Embedded 
11. Support Third Party APIs(Pandas, Scipy, Matplotlob, numpy, scikit)

"""
# If you're trying to use the Python random module (which is part of the standard library and doesn't require installation)
import random
print(random.randint(1,10))

"""
A Collector is one of the software component in python software which is running in the background of regular python program and whose role is
to collect/remove unused memory space"""

# adding element
a1 = [1,3,4,5,65,6]
b1 = [5,6,7,8,9]
print(type(a1.append(b1)))
print(a1)

# such metods perform their effect by altering the list in-place, not by building and returning a new one.
a1.insert(2,b1)
print(a1)

# pop removing the top most/latest element - inplace
a1.pop(2)
print(a1)

# extend
a1.extend(b1)
print(a1)

