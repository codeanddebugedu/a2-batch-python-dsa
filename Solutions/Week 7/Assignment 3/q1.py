from typing import List


class Book:
    def __init__(self, isbn, name, price, quantity):
        self.isbn = isbn
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_rented = False


library: List[Book] = []


def addBook(isbn, name, price, quantity):
    for book in library:
        if book.isbn == isbn:
            print("Book with this ISBN already exists in the library.")
            return
    new_book = Book(isbn, name, price, quantity)
    library.append(new_book)
    print("Book added successfully.")


def searchBook(isbn):
    for book in library:
        if book.isbn == isbn:
            print(
                f"Book found:\nISBN: {book.isbn}\nName: {book.name}\nPrice: {book.price}\nQuantity: {book.quantity}"
            )
            return
    print("Book with this ISBN not found in the library.")


def checkQuantity(isbn):
    for book in library:
        if book.isbn == isbn:
            print(f"Quantity of book with ISBN {isbn}: {book.quantity}")
            return
    print("Book with this ISBN not found in the library.")


def rentBook(isbn):
    for book in library:
        if book.isbn == isbn:
            if book.quantity > 0:
                book.quantity -= 1
                book.is_rented = True
                print("Book rented successfully.")
                return
            else:
                print("Book is not available for rent.")
                return
    print("Book with this ISBN not found in the library.")


def displayBooks():
    if not library:
        print("Library is empty.")
        return
    print("Books in the library:")
    for book in library:
        print(
            f"ISBN: {book.isbn}\nName: {book.name}\nPrice: {book.price}\nQuantity: {book.quantity}\nIs Rented: {'Yes' if book.is_rented else 'No'}\n"
        )


def exitProgram():
    print("Exiting program.")
    exit()


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Check Quantity")
    print("4. Rent Book")
    print("5. Display Books")
    print("6. Exit Program")

    choice = input("Enter your choice: ")

    if choice == "1":
        isbn = input("Enter ISBN: ")
        name = input("Enter name: ")
        price = input("Enter price: ")
        quantity = int(input("Enter quantity: "))
        addBook(isbn, name, price, quantity)
    elif choice == "2":
        isbn = input("Enter ISBN to search: ")
        searchBook(isbn)
    elif choice == "3":
        isbn = input("Enter ISBN to check quantity: ")
        checkQuantity(isbn)
    elif choice == "4":
        isbn = input("Enter ISBN to rent: ")
        rentBook(isbn)
    elif choice == "5":
        displayBooks()
    elif choice == "6":
        exitProgram()
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
