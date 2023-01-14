#__str__ and  __repl__ methods  
class  Student:
    def __init__(self , name  , age ):
        self.name   = name   
        self.age    = age   
    
    def __str__(self):
        return  f"My name is {self.name} and i am  {self.age} years old" 
    
    def __repr__(self) -> str:
        return  f"<Person({self.name}  ,  {self.age}>"  #used   in python debugging 
    
    
s1  =  Student("mayur" , 22)
print(s1)