# we can  pass funtions  with multiple parametrs in the decorator using  *args  and  *kwargs as  a  parameter  inside the decorator func 



user  =  {
    'username' :  'mayur'  , 
    'access level' :  'admin'  
    
}



def make_secure(func):
    def secure_function(*args  ,  **kwargs ):
        if user['access level'] == 'admin':
            return func(*args  ,  **kwargs)  
        else:
            return  f"no admin Password access to  {user['username']}"        
    return  secure_function


@make_secure
def get_password(panel):
    if panel ==  'admin':
        return 1234 
    elif panel  == 'billing':
        return "super secure password"  

#get_admin_password  =  make_secure(get_admin_password)   now  as the @ is  used we  dont need to do this   

print(get_password('admin'))