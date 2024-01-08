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

# such meth
# ods perform their effect by altering the list in-place, not by building and returning a new one.
a1.insert(2,b1)
print(a1)

# pop removing the top most/latest element - inplace
a1.pop(2)
print(a1)

# extend
a1.extend(b1)
print(a1)

# dictionary : get(), values(), keys(), items(), pop(), popitem(), clear(), update(), copy()

dict_1 =   {"key1": [1,2,3,4,5], "key2":[9,7,5,4,3]}
print(dict_1)

print(dict_1.get("key2")) # key value
print(dict_1.keys())
print(dict_1.items())
print(dict_1.pop("key1"))# removes the key value pair
print(dict_1)

dict_2 =   {"key1": [1,2,3,4,5], "key2":[9,7,5,4,3]}
print(dict_2.popitem())
print(dict_2)


nom = int(input("Enter how many nultiplication tables you want:"))
if(nom<=0):
    print("{}invalid input".format(nom))
else:
    for n in range(1,nom+1):
        print("________________________")
        print("\t Mul table for:{}".format(n))
        print("________________________")
        for i in range(1,11):
            print("\t{}X{}={}".format(n,i,n*i))
        else:
            print("_____________________")    
            
