Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(10+20)
30
a=10
b=20
c=a+b
print(c)
30
d=b-a
print(d)
10
e=a*b
print(e)
200
f=b/a
print(f)
2.0
print(20+30)
50
print(20-10)
10
print(40/20)
2.0
print(20*10)
200
a=10
b=20
c=30
d=40
print(a+b-c/d)
29.25
print(a+b,b-c)
30 -10
print(a\b)
SyntaxError: unexpected character after line continuation character
a=10
b=1.55
c="hello"
d=True
e=10+2j
print(a)
10
prnit(type(a))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    prnit(type(a))
NameError: name 'prnit' is not defined. Did you mean: 'print'?
print(type(a))
<class 'int'>
>>> print(b)
1.55
>>> Print(typr(b))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Print(typr(b))
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print(type(b))
<class 'float'>
>>> print(c)
hello
>>> print(type(c))
<class 'str'>
>>> print(d)
True
>>> print(type(d))
<class 'bool'>
>>> print(e)
(10+2j)
>>> print(type(e))
<class 'complex'>
>>> print(type(a),type(b))
<class 'int'> <class 'float'>
>>> print(a,b,c,d,e)
10 1.55 hello True (10+2j)
>>> peint(a\nb)
SyntaxError: unexpected character after line continuation character
>>> print(/n a)
SyntaxError: invalid syntax
>>> a=input("enter the value of a ")
enter the value of a 10
>>> print(a)
10
>>> primt(type(a))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    primt(type(a))
NameError: name 'primt' is not defined. Did you mean: 'print'?
>>> print(type(a))
<class 'str'>
>>> a=int(input("a is"))
a is5
>>> b=int(input("b is"))
b is2
>>> print(a**b)
25
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=input()
print(a)
10
10
a=input("enter the value")
enter the value10
print(a)
10
a=input(enter the value)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(type(a))
<class 'str'>
a=int(input(enter the value))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=int("input(enter the value)")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a=int("input(enter the value)")
ValueError: invalid literal for int() with base 10: 'input(enter the value)'
a=int(input("enter the value"))
enter the value10
print(type(a))
<class 'int'>
a=flat(input("enter the value"))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a=flat(input("enter the value"))
NameError: name 'flat' is not defined. Did you mean: 'float'?
a=float(input("enter the value"))
enter the value10
print(type(a))

<class 'float'>
a=bool(input("enter the value"))
enter the valueTrue
print(type(a))

<class 'bool'>
a=comp(input("enter the value"))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a=comp(input("enter the value"))
NameError: name 'comp' is not defined
a=complex(input("enter the value"))
enter the value10
a=complex(input("enter the value"))

enter the value10-9j


#take 2 integers input from the user and print the quotient and remainder when a/b



a=int(input("enter a"))
b=int(input("enter b"))
if a%2==0 and b%2==0:
    print("even")
else:
    print("odd")
    




        

        
        
    
        

