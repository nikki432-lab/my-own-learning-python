Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =10
>>> b= 5
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(a,b)
5 10
>>> a=10
>>> b=5
>>> temp=a
>>> a=b
>>> b=temp
>>> print(a,b)
5 10
>>> a=10
>>> b=5
>>> a=a^b
>>> b=a^b
>>> a=a^b
>>> print(a,b)
5 10
>>> a=10
>>> b=5
>>> a,b=b,a
>>> print(a,b)
5 10
