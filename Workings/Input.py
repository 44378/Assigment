Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Jack Scaife
>>> #09/09/2014
>>> #Input test 1
>>> print(Command)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(Command)
NameError: name 'Command' is not defined
>>> file(Command.py)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    file(Command.py)
NameError: name 'file' is not defined
>>> print(Command.py)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(Command.py)
NameError: name 'Command' is not defined
>>> ================================ RESTART ================================
>>> 
Hello world
Please input your nameJack
Traceback (most recent call last):
  File "U:/Computing/GitEye - Storage/.gitconfig/Workings/Assigment/Workings/Command.py", line 3, in <module>
    print("Hello {0}!".fromat(first_name))
AttributeError: 'str' object has no attribute 'fromat'
>>> ================================ RESTART ================================
>>> 
Hello world
Please input your name Jack
Traceback (most recent call last):
  File "U:/Computing/GitEye - Storage/.gitconfig/Workings/Assigment/Workings/Command.py", line 3, in <module>
    print("Hello {0}!".fromat(first_name))
AttributeError: 'str' object has no attribute 'fromat'
>>> ================================ RESTART ================================
>>> 
Hello world
Please input your nameJack
Hello Jack!
>>> 
