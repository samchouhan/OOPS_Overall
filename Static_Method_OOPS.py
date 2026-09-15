#Methods that do not have self parameter(Work at class level)
"""
class Student:

    def show(self):
        print("Object is:", self)

s1 = Student()
s1.show()
"""
class student:
    @staticmethod
    def show():
        print("This is static method")


s1 = student()
s1.show()
