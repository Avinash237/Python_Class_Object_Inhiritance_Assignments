"""
OOP:-
"""
"""
oop Properties/ piller of OOP
-   Inhiritance
-   Encapsulation
-   Abstraction
-   Plymorphism


-------------------------------------------------------------------

-   Inhiritance: building parent child relationshipp amoung the classes 
-   due to inhiritance, we can acess member of parent class 
---------------------------------------------------------------
eg:
    
class RBI:  # parent class/root class
    def fund(self):
        print('funds from RBI')
class SBI(RBI):  # child class/derrived class
    pass
s1 = SBI()
s1.fund()
---------------------------------------------------------------------

# Multilevel inhiritance
class Director:
    def admin_help(self):
        print('Director Help')
class principle(Director):
    def cancle_admission(self):
        print('Aprived/disaproved')
    def leave(self):
        print('principle:leave approval')

class Teacher(principle):
    def leave(self):
        print('teacher: leave approval')

class student(Teacher):
    pass

s = student()
s.admin_help()
s.leave()
---------------------------------------------------------


# multilevel inhiritance
-   SuperParent<--Parnt<--child
ex.
    - we have multiple parent and 1 child
ex.
-----------------------------------------------------------------
class SP:
    def call_1(self):
        print('sharad pawar NCP')

class AP(SP):
    def call_2(self):
        print('Ajit Pawar NCP')

class party(AP):
    pass

p = party()
p.call_1()
-----------------------------------------------------------------

# Multiple inhiritance 
-   More Than one parent 
ex.

class Mother:
    def Money(self):
        print('Mother Money')

class father:
    def money(self):
        print('father money')
    def car(self):
        print('father car')

class child(Mother,father):
    def m1(self):
        father.money(self)

c = child()
c.Money()
c.car()
c.m1()
--------------------------------------------------------------------------
"""

class Mother:
    def money(self):
        print('Mothers Money')

class Father(Mother):
    def money(self):
        print('Father Money')
        super().money()

    def car(self):
        print('Fathers car')


class Child(Father):
    pass

c = Child()
c.money()
c.car()






































