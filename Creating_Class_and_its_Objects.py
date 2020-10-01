#Creating a Fan class in Python
class Fan:     

    #Constructor of Fan Class          
    def __init__(self):        
        self.color="Blue"
        self.brand="Usha"
        self.cost=2500

#Creating Object for the Fan Class       
fanObj=Fan()                    

#Accessing the Instance Variables using Object of Fan Class
print(fanObj.color)             
print(fanObj.brand)
print(fanObj.cost)