#wrapping data and functions into single unit (object) is called encapsulation
class Student:
    def __init__(self,name,marks):
        self.__name=name#private attribute
        self.__marks=marks#private attribute
        
        
    def show_marks(self):
        print("Marks:",self.__marks)
        
    def update_marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self.__marks=new_marks
        else:
            print("Invalid marks. Please enter marks between 0 and 100.")
            
s1=Student("Peter Parker",[85,90,78])
s1.show_marks()