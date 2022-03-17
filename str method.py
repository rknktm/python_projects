class Book:
    def __init__(self,title,autor,page,publisher):
        print("init funktion is working\n")
        self.title=title
        self.autor=autor
        self.page=page
        self.publisher=publisher
        
    def __str__(self):
        return f"Title:{self.title}\nAutor:{self.autor}\nPage:{self.page}\nPublisher:{self.publisher}"
    
book1=Book("Kasagi","Ömer Seyfettin",114,"Sevgi Yayinlari")
print(book1)   
     