"""
Advance Python
- OOP Object Oriented Programing
"""
"""
-  Object: am entity which exist physically in the environment

f = 54 # everything is a object in a python
-    each object has predefined structure and that structure is called class
-   class is template/bluprint/structure
-   using class we can create object
"""
"""
- class is a container which contains properties(variable) + behaviour(methods)
- 
---------------------------------------------------------------------------
class Human:
    #properties
    legs = 2
    hand = 2
    head = 1

    #operation/behaviour
    def talk(self):
        print('start talking')
    def sleep(self):
        print('start sleeping')
    def work(self):
        print('start working')

# to allocate a memory to a class
# create the constructor
# constructor is same name as that of class name
# constructor == className() class calling
p1 = Human()    # p1 is a object of Human class
print(p1)
print(dir(p1))
p1.talk()
print(p1.head)
"""
"""
----------------------------------------------------------------------------
-   first we have to create class
-   ir has a specified structure
-   we can acesss member of a class using a constructor
-   when constructor gets called an object gets created automatically 
-   in above case p1 is an object and human() is a cnstructor

---------------------------------------------------------------------------------
-   we can create number of objects 
-   so we must have to call multiple constructure

-------------------------------------------------------------------
class Human():
    #properties
    legs = 2
    hands = 2
    head = 2

    # operation/behaviour
    def talk(self):
        print('start talking')

    def sleep(self):
        print('start sleeping')

    def work(self):
        print('start working')

janta = Human()
print(janta.head)
janta.sleep()
print('-----------------------')
ravan = Human()
ravan.head = 10
print(ravan.head)
print(Human.head)
ravan.talk()
----------------------------------------------------

-    what is self?
        - it is a reference variable inside a method 
        -  used to access member of a class insidea method
        
-    it is a prevent in instance method 
-   instance method is a method whose structure can be changed        
-------------------------------------------------------------
class sample:
    a = 10   # class level variable

    def show(self):
        # access in show
        print('show')
        print(self.a)

    def test(self):
        #call show from test
        print('test')
        self.show()
s1 = sample()
s1.show()
s1.test()
-----------------------------------------------------------
-   what is __init__ method:
-   it is a method associated with constructor
-   meanse when we call constructor then init method gets call automatically
ex.
-------------------------------------------------------------
class sample:
    def __init__(self):
        print('init called')
sample()  ## just created object and init is called
sample()
--------------------------------------------------------------
-   can we pass values to method/constructor
-   Ans: yes

"""
class sample:
    def __init__(self,name,age,salary):
        print(name,age,salary)

sample('Sunita',30,10000)
sample(age=30,salary=63000,name='sahil')

