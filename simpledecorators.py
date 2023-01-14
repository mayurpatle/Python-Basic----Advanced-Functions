#decorators  are used when are to  rpovide access to any parameter    inside  the  function 
user  =  {
    'username' :  'mayur'  , 
    'access level' :  'admin'  
    
}


def get_admin_password():
    return  1234  

def make_secure(func):
    def secure_function():
        if user['access level'] == 'admin':
            return func()  
        else:
            return  f"no admin Password access to  {user['username']}"        
    return  secure_function

get_admin_password  =  make_secure(get_admin_password)
print(get_admin_password())
    