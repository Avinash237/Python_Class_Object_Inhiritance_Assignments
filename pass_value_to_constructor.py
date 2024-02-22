class Sample:
    def __init__(self,name,age,salary):
        print(name,age,salary)

    def show(self,id,roll):
        print(id,roll)


Sample('amit',44,98000)
Sample(age=23,salary=45000,name='hitesh')

s1 = Sample(name='sagar',age=32,salary=88000)
s1.show(111,31)

