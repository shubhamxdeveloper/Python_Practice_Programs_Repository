#Creating Fan class
class Fan:
    #Creating Constructor of the class having Instance Variable    
    def __init__(self):
        self.color="Blue"
        self.brand="Usha"
        self.cost=2500

#Creating Object from the Class
fanObj1=Fan()

fanObj2=fanObj1

#Printing the Address of the Objects
print(fanObj1)

print(fanObj2)

#Printing the IDs of the Objects
print(id(fanObj1))

print(id(fanObj2))

#Checking using IS Operator which returns Boolean Values TRUE or FALSE
print(fanObj1 is fanObj2)