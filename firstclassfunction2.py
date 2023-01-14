def search(sequence  ,  expected , finder ):
    for i  in sequence :
        if finder(i) == expected:
            return i  
        raise RuntimeError(f"could  not  find element wwoth {expected}")


friends  = [
    { "name" :  "mayur patle"  , "age" : 22  }  ,  
    {
        "name" :   "rolf smith"  ,  "age" : 25 
    },
    {
        "name" :   "anne pun"  ,  "age" : 22
    }
    ]


def get(friend):
    return  friend["name"]


print(search(friends , "mayur patle"  ,  get ))