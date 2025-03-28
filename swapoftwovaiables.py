swap of two variables without using third variable
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
