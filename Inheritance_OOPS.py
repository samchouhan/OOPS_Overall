class Employee:
    def __init__(Self,name,salary):
        Self.name=name#private attribute
        Self.salary=salary#private attribute
    def display_info(Self):#To display the given attributes of the classes to the user a data.
        print("Name:",Self.name)
        print("Salary:",Self.salary)
        
    def show_name(Self):
        print(sorted([Self.name]))
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

for employee in employees:#With this for loop blcok we can now manage many employees data withing a list system , this list will keep updating and we will know the present employess of the company.
    employee.display_info()
    
    
 
    
#We can also add methods to add or delete employess from the comapny list, and also we can add methods to update the employee data.