class Student:
#class main
    def __init__(self,id,name): #default constrct 
        self.id=id
        self.name=name
    def print(self):            #method 
        print(self.name,self.id)

        # here int the print method we are calling the class.name and class.id 

#self is used to point within class details 
# self.name is refering to class.name 

ram=Student(18003085,"Ramgopal tummala") 
#creating objcts to the class
ram.print()
#calling the print method 
