class bookshelf:
    def __init__(self , *books):
        self.books =  books
        
    def __str__(self):
        return  f"bookshlf with  {len(self.books)} books"
    
shelf  = bookshelf(300)

print(shelf)


class book:
    def __init__(self  , name  ):
        
        self.name =  name  
        
    def __str__(self):
        return  f"book {self.name}"
    
    
book1 =  book("harry potter")
book2 =  book("python  101")  
shelf  =  bookshelf(book1  , book2 )

print(shelf)