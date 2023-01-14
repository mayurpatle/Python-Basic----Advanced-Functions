class Device:   #this  is the parent class 
    def __init__(self ,  name ,  connected_by ):
        self.name = name   
        self.connected_by =  connected_by
        self.connected = True   
        
    def __str__(self):
        return f"Device {self.name}  ({self.connected_by})"
    
    def disconnect(self):
        self.connected  =  False 
        print("Device  got Disconnected")
        
        
     
    



class Printer(Device):    #this is  the syntax of the  child  class  
    def __init__(self ,  name ,  connected_by  ,  capacity):
        super().__init__(name  , connected_by)   #super  method is used to inherit the properties   
        self.capacity =capacity  
        self.remaining_pages  = capacity 
        
    def  __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages  remaining"
    
    def print(self , pages ):
        if not self.connected:
            print("your printer is not connected")
            return  
        print(f"Printing  {pages} pages")
        self.remaining_pages -=  pages  
    
p1 = Printer("Printer" ,  "usb" ,  1500)
print(p1)
p1.print(56  )
print(p1)