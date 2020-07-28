class Book:
    
    def __init__(self):
        print("Book object created")
    
    def getBook(self):
        self.bid=input("Enter Book Id=>")
        self.bname=input("Enter Book Name=>")
        self.price=input("Enter Price=>")
        self.auther=input("Enter Author=>")
        self.edition=input("Enter Edition=>")

    def printBook(self):
        print("Book  id=",self.bid)
        print("Book  Name=",self.bname)
        print("Book  Price=",self.price)
        print("Book  Author=",self.auther)
        print("Book  Edition=",self.edition)

booklist=list()
def main():
    while True:
        print("***************Book Management System**************")
        print("1.for Add Book")
        print("2.for Update Book")
        print("3.for Delete Book")
        print("4.for Search Book")
        print("5.for Show all BookList")
        print("6.for Exit")
        ch=int(input("Enter choice=>"))
        if ch==1:
            b1=Book()
            b1.getBook()
            booklist.append(b1)
            print("Book added successfully in list...........!")
        elif ch==2:
            eid=input("Enter Book Id want to update=>")
            for i in booklist:
                if eid==i.bid:
                    while True:
                        print("1.Update Book ID")
                        print("2.Update Book Name")
                        print("3.Update Book Price")
                        print("4.Exit")
                        ch=int(input("Enter your choice=>"))
                        if ch==1:
                            b=int(input("Enter New Book ID=>"))
                            i.bid=b
                            print("Book ID Updated successfully in list...........!")
                        elif ch==2:
                            b=input("Enter New Book Name=>")
                            i.bname=b
                            print("Book Name Updated successfully in list...........!")
                        elif ch==3:
                            b=int(input("Enter New Book Price=>"))
                            i.price=b
                            print("Book Price Updated successfully in list...........!")
                        elif ch==4:
                            break
                        else:
                            print("Enter Invalid choice....!")
                        print("*************************************")
                        
                else:
                    print("Book Not Found")
            
                
        elif ch==3:
           eid=int(input("Enter Book Id want to Delete=>"))
           for i in booklist:
                if eid==i.bid:
                    booklist.remove(i)
                else:
                    print("Book NOT found")
        elif ch==4:
            eid=int(input("Enter Book Id want to Search=>"))          
            for i in booklist:
               if i.bid==eid:
                   i.printBook()

               else:
                    print("Book Not Found")
           
            
        elif ch==5:
            for i in booklist:
                i.printBook()
        elif ch==6:
            break
        else:
            print("choice not Available.....!")


if __name__=='__main__':
    main()
            
