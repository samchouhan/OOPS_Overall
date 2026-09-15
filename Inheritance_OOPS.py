class Employee:
    def __init__(Self,name,salary):
        Self.__name=name#private attribute
        Self.__salary=salary#private attribute
    def display_info(Self):
        print("Name:",Self.__name)
        print("Salary:",Self.__salary)
class Developer(Employee):
    def __init__(self,name,salary,language):
        self.language=language
        super().__init__(name,salary)
        
    def display_info(Self):
        super().display_info()
        print("Programming Language:",Self.language)
        
        
class manager(Employee):
    def __init__(self,name,salary,Teamsize):
        self.Teamsize=Teamsize
        super().__init__(name,salary)
        
e1=Employee("Patrick Jane",50)
e1.display_info()
