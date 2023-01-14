# functools is a  library  that  wraps  the decorator function  to the funtion that is  being passed  in the  decoreator 
import functools 
user  =  {
    'username' :  'mayur'  , 
    'access level' :  'admin'  
    
}



def make_secure(func):
    @functools.wraps(func)
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

print(get_admin_password.__name__)
