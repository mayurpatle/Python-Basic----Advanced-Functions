#factory example  
class Book:
    types = ("harcover" ,  "paperback")
    
    def __init__(self , name ,  book_type ,  weight):
        self.name    = name  
        self.book_type =  book_type
        self.weight  =  weight  
     
    def __repr__(self):
        return  f"<Book  {self.name} , ,  {self.book_type}  ,  {self.weight}  g>  "  
    
    @classmethod
    def hardcover(cls,  name  ,  page_weight):
        return cls(name ,  cls.types[0] , page_weight + 100)
    
    @classmethod
    def paperback(cls , name ,  page_weight):
        return  cls(name  ,  cls.types[1]  , page_weight )
     
book  =  Book.hardcover("Harry potter"   , 1500 )
print(book.name)
print(book)


book1  =  Book.paperback("python 101" ,  600)
            