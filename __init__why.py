#This program shows the significance of __init__() method.

# Without __init__()
"""
class Student:
    pass

s1 = Student()

s1.name = "Sam"
s1.age = 19

print(s1.name)
print(s1.age)

Here we have to assign values manually to the attributes

"""
#Now with __init__()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
s1 = Student("Sam",19)
print(s1.name)
print(s1.age)

#Here we did not have to assign values manually to the attributes, we just passed the values as arguments to the __init__() method and it automatically assigned them to the attributes.
