class LIBRARY:
    def __init__(self,list_of_books):
        self.books_list=list_of_books

    def available_books(self):
        for i in range(0,len(self.books_list)):
            print(i+1,".",self. books_list[i])


    def borrow_book(self,book_name):
        if book_name in self.books_list:
            print("You Have successfully borrowed the book.")
            print("Make sure that you return" ,book_name," before the deadline")
            self.books_list.remove(book_name)
            return True

        else:
            print("Sorry cannot find the book: ", book_name)
            return False

    def return_book(self,book_name):
        print("Thanks for returning ", book_name)

        self.books_list.append(book_name)

        print(book_name," has been added to Library")

class STUDENT:
    def request_book(self):
        self.book=input("Enter the name of the book: ")
        return self.book.lower()
    def return_book(self):
        self.book = input("Enter the name of the book: ")
        return self.book.lower()
if __name__ =="__main__":
    Books_in_Library=["atomic habits","how to talk to anyone","psychology of money","the power of your subconcious mind","attitude is everything","think and grow rich"]
    central_library=LIBRARY(Books_in_Library)
    student=STUDENT()
    while(True):
        Welcome_msg=''' \nWelcome!
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        
        '''


        print(Welcome_msg)
        i_p=int(input("What would you like to do?  "))

        if i_p==1:
            central_library.available_books()
        elif i_p==2:
            central_library.available_books()
            central_library.borrow_book(student.return_book())
        elif i_p==3:
            central_library.return_book(student.return_book())

            central_library.available_books()
        else:
            print("Invalid Choice")
        print()
        decision=input("DO YOU WANT TO CONTINUE ? PRESS C TO CONTINUE OR SOMETHING ELSE TO EXIT  ")

        if decision=='c' or decision=='C':
            continue
        else:
            break




