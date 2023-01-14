#with  @ suntax for decorators  we can directly mention that the func  will be  gonna passed to  decorator 
#decorators  are used when are to  rpovide access to any parameter    inside  the  function 
user  =  {
    'username' :  'mayur'  , 
    'access level' :  'admin'  
    
}



def make_secure(func):
    def secure_function():
        if user['access level'] == 'admin':
            return func()  
        else:
            return  f"no admin Password access to  {user['username']}"        
    return  secure_function


@make_secure
def get_admin_password():
    return  1234  

#get_admin_password  =  make_secure(get_admin_password)   now  as the @ is  used we  dont need to do this   

print(get_admin_password())
