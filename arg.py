#args return the  tuple  of all the arguemnets  that  you  pass to the func that has  a parameter    of arg 

#for example  
def add( *args):
    temp  =  0 
    for i  in args:
        temp  += i 
    print(temp) 
    
add( 1  ,2  , 3 , 4 , 5 )

#how gto pass  a tuple as  a  argument  

def detail(*args):
    print(args) 
    
    
tuple  =  ( 1  , 3  , 5 ,   7  )   
detail(*tuple)   