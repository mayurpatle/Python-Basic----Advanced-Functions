class Classtest:
    def instance_method(self):   #used for data inside the objects  
        print(f"Called  instance_method of  the {self} ")
    
    @classmethod          #takes the parameter  claass  itself 
    def class_method(cls):  #used often as  factories  -- 
        print(f"Called class_method  of {cls}")
     
    @staticmethod
    def static_method():  #static  methisd does not takes  any parameter  '
        print(f"Called  Static_method.")
    
       
Classtest.class_method() 
Classtest.static_method()
