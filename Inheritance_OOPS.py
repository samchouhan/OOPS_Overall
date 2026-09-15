class Employee:
    def __init__(Self,name,salary):
        Self.__name=name#private attribute
        Self.__salary=salary#private attribute
        
class Developer(Employee):
    def __init__(self,name,salary,language):
        self.language=language
        super().__init__(name,salary)
        
        
class manager(Employee):
    def __init__(self,name,salary,Teamsize):
        self.Teamsize=Teamsize
        super().__init__(name,salary)
        
