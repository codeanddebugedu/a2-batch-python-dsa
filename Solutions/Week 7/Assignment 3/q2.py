class Bookstore:
    def __init__(self):
        self.inventory = {}
        self.salesData = []

    def addBook(self, isbn, name, author, price, quantity):
        if isbn in self.inventory:
            print("Book with this ISBN already exists in the inventory.")
            return
        self.inventory[isbn] = {
            "name": name,
            "author": author,
            "price": price,
            "quantity": quantity,
        }
        print("Book added successfully.")

    def searchBook(self, criteria):
        foundBooks = []
        for isbn, details in self.inventory.items():
            if criteria.lower() in [
                isbn.lower(),
                details["name"].lower(),
                details["author"].lower(),
            ]:
                foundBooks.append((isbn, details))
        if foundBooks:
            print("Matching books found:")
            for isbn, details in foundBooks:
                print(
                    f"ISBN: {isbn}, Name: {details['name']}, Author: {details['author']}, Price: {details['price']}, Quantity: {details['quantity']}"
                )
        else:
            print("No matching books found.")

    def updateQuantity(self, isbn, newQuantity):
        if isbn not in self.inventory:
            print("Book with this ISBN does not exist in the inventory.")
            return
        self.inventory[isbn]["quantity"] = newQuantity
        print("Quantity updated successfully.")

    def processOrder(self, isbn, quantity, customerName):
        if isbn not in self.inventory:
            print("Book with this ISBN does not exist in the inventory.")
            return
        if self.inventory[isbn]["quantity"] < quantity:
            print("Insufficient quantity available.")
            return
        totalPrice = self.inventory[isbn]["price"] * quantity
        self.inventory[isbn]["quantity"] -= quantity
        self.salesData.append(
            {
                "ISBN": isbn,
                "Customer": customerName,
                "Quantity": quantity,
                "Total Price": totalPrice,
            }
        )
        print("Order processed successfully.")

    def getSalesReport(self):
        totalRevenue = sum(transaction["Total Price"] for transaction in self.salesData)
        totalBooksSold = sum(transaction["Quantity"] for transaction in self.salesData)
        print("Sales Report:")
        print(f"Total Revenue: {totalRevenue}")
        print(f"Total Books Sold: {totalBooksSold}")

    def displayInventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for isbn, details in self.inventory.items():
            print(
                f"ISBN: {isbn}, Name: {details['name']}, Author: {details['author']}, Price: {details['price']}, Quantity: {details['quantity']}"
            )

    def displaySalesData(self):
        if not self.salesData:
            print("No sales data available.")
            return
        print("Sales Data:")
        for transaction in self.salesData:
            print(
                f"ISBN: {transaction['ISBN']}, Customer: {transaction['Customer']}, Quantity: {transaction['Quantity']}, Total Price: {transaction['Total Price']}"
            )


bookstore = Bookstore()
while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Update Quantity")
    print("4. Process Order")
    print("5. Generate Sales Report")
    print("6. Display Inventory")
    print("7. Display Sales Data")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        isbn = input("Enter ISBN: ")
        name = input("Enter name: ")
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        bookstore.addBook(isbn, name, author, price, quantity)
    elif choice == "2":
        criteria = input("Enter ISBN, name, or author to search: ")
        bookstore.searchBook(criteria)
    elif choice == "3":
        isbn = input("Enter ISBN of the book to update quantity: ")
        newQuantity = int(input("Enter new quantity: "))
        bookstore.updateQuantity(isbn, newQuantity)
    elif choice == "4":
        isbn = input("Enter ISBN of the book to process order: ")
        quantity = int(input("Enter quantity: "))
        customerName = input("Enter customer name: ")
        bookstore.processOrder(isbn, quantity, customerName)
    elif choice == "5":
        bookstore.getSalesReport()
    elif choice == "6":
        bookstore.displayInventory()
    elif choice == "7":
        bookstore.displaySalesData()
    elif choice == "8":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
