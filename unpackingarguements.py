def multiply(*args):
    product  = 1  
    for arg  in args:
        product   = product  * arg
    print(product)
    
multiply(3  , 4 , 5  )

def add(x  ,  y  ):
    temp  =    x + y  
    print(temp) 
    
dict  = {
    "x"  :   10  , 
    "y"  : 15 
}

add(**dict)


