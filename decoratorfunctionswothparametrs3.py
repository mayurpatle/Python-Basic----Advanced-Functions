user  =  {
    'username' :  'mayur'  , 
    'access level' :  'guest'  
    
}


def  make_secure(access):
    def decorator(func):
        def secure_function():
            if user['access level'] == access:
                return func()  
            else:
                return  f"N0 !!  {access} access to  {user['username']}"        
        return  secure_function
    
    return  decorator


@make_secure('admin')
def get_admin_password():
    return  1234  


@make_secure('guest')
def get_guest_password():
    return  "abcd"

#get_admin_password  =  make_secure(get_admin_password)   now  as the @ is  used we  dont need to do this   

print(get_admin_password())
print(get_guest_password())