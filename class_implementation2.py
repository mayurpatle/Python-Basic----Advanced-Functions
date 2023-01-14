class Student:
    def __init__(self ,name ,  age  ):   #self is  a  parameter  that is  always given , self is  the obkect here  passed  , init  act  as  a  constructor  
        
        self.name = name   
        self.age = age 
        self.grades =  ( 99 ,  98 , 92 ,  91 ,  90 ) 
        
    def  average(self):
        print(sum(self.grades) / len(self.grades))
    
S1  = Student( "rohit"  ,  45  ) 
print(S1.__dict__) # print  all the  attributes  of the  objects in the  form pf  a  dicrtionary 
S1.likes  =  ["cricket"   ,  "love stories"] #attributes  can be  passe carbitarily  

print(S1.likes)  
S1.average()   