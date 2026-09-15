#Hiding the implementation details from the user is called abstraction.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
        
        
    def start(self):
        self.acc=True#here these things were only seen for us not the user 
        self.brk=False#The user just gets to know the car has started
        self.clutch=True
        print("Car is started!🏎️💨𝑅𝐴𝑇𝐴𝑇𝐴𝑇𝐴𝑇𝐴𝑇𝐴")
        
car1=Car()
car1.start()