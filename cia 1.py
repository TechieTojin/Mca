
#1
ordered_part=['Start','River']
jumbled_part=['Clearing','Village','Cave']
correct=[]
def reconstruct_path(ordered_part,jumbled_part):
    for i in jumbled_part:
        ordered_part.append(i)
    ordered_part.insert(1,'Clearing')
    ordered_part.insert(3,'Village')
    ordered_part.insert(4,'Cave')
    for i in ordered_part:
     if i not in correct:
        correct.append(i)
    print(correct)
    
reconstruct_path(ordered_part,jumbled_part)


#2
class LibraryItem:
    def __init__(self,title):
        self.title=title
    def GetDetails(self):
        print("Book details:")
        print(f"Title:{self.title}")
        
class Book(LibraryItem):
    
    def __init__(self,title,author,genre,isbn):
        super().__init__(title)
        self.author=author
        self.genre=genre
        self.isbn=isbn

    def Checkout(self):
        availability=False
        print("Book checked out")

    def ReturnBook(self):
        availability=True
        print("Book returned")

    def UpdateAvailability(self,new_status):
        if new_status==False:
            print("Book is currently checked out")
        else:
            print("Book is available")

    def GetDetails(self):
        print("Book details:")
        print(f"Title:{self.title}\nAuthor:{self.author}\nGenre:{self.genre}\nISBN:{self.isbn}")

    def AddToLibrary(self):
        print(f"Book added to library:{self.title}")
        
o1=Book("physics","RK Murthy","educational",1234)
o2=Book("Grandmas bag of stories","sudha Murthy","fiction",1114)

o1.GetDetails()
o1.Checkout()
o1.UpdateAvailability(False)
o1.ReturnBook()
o1.AddToLibrary()
print()
o2.GetDetails()
o2.Checkout()
o2.UpdateAvailability(True)
o2.ReturnBook()
o2.AddToLibrary()



#3
class LibraryItem:
    def get_details(self):
        print("Libaray Items are here.")

class Magazine(LibraryItem):
    def __init__(self,issue_number):
        self.issue_number=issue_number
    def get_details(self):
        print(f"issue_number:{self.issue_number}")

class DVD(LibraryItem):
    def __init__(self,duration):
        self.duration=duration
    def get_details(self):
        print(f"duration:{self.duration}")
    

ob1=Magazine(1234)
ob2=DVD("30 min")
ob1.get_details()
ob2.get_details()
    

    

    
            
