#Create student class that takes name and marks of 3 subjects as 
#arguments in constructor , then create method to print average marks of student.
class Student:
    def __init__(self,name,marks):
        self.name = name#Attribute to store name of student
        self.marks = marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Average marks of ",self.name,"is",sum/3)
        
s1=Student("Peter Parker",[85,90,78])
s1.get_avg()

s1.name="Spider Man"#Updating name of student
s1.get_avg()