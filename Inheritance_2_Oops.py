class Spiderman:
    def swing(self):
        print("Swinging through the city!")
        
        
class Spider(Spiderman):
    def Webbing(self):
        print("Organic webbing activated!")
        
a1=Spider() 

a1.swing()  # Inherited method from Spiderman class
a1.Webbing()  # Method defined in Spider class