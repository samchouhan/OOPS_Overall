class Employee:
    def __init__(Self,name,salary):
        Self.name=name#private attribute
        Self.salary=salary#private attribute
    def display_info(Self):
        print("Name:",Self.name)
        print("Salary:",Self.salary)
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
    def display_info(Self):
        super().display_info()
        print("Team Size:",Self.Teamsize)
        
        
e1=Employee("Patrick Jane",50)
e1.display_info()

d1=Developer("Alice Smith",60000,"Python")
m1=manager("Bob Johnson",80000,10)
d2=Developer("Charlie Brown",70000,"Java")
m2=manager("David Wilson",90000,15)

employees=[d1,m1,d2,m2]