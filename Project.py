books = {
    1: "Pesawat Jahanam",
    2: "Titisan Mc",
    3: "Jujur Saya kasihan",
    4: "Cara Menjadi Hokage No Root"
}

allow_duplicates = False

def view():         
    if books:
    
        if books:
            print("Daftar Buku:")
        for book_id, book_name in books.items():
            print(f"Book ID: {book_id} - Book Name: {book_name}")
        
        search_name = input("Enter the book name to search: ")
        search_results = [book_name for book_name in books.values() if book_name == search_name]
        
        if search_results:
            print(f"The book '{search_name}' is found in the library.")
        else:
            print(f"The book '{search_name}' is not found in the library.")
    
    else:
        print("No books available.")
    
    
    
      
    back2menu()


def addBook() :
    dupli=input("Duplikasi (yes/no):")
    if dupli=='yes':
        turnOnDups()
    elif dupli=="no":
        print("No Duplicate!")
    else:
        print("error")    
    book_name= input('Masuukan Nama Buku: ')
    if not allow_duplicates and book_name in books.values():
        print("Book already exists in the library.")
        
    simpan=input("\napakah anda ingin save? (Y/N): ")
    if simpan =="Y":
            book_id = max(books.keys()) + 1 if books else 1
            books[book_id] = book_name
            print(f"Book '{book_name}' added successfully.")
    else :
        print("Book Not Saved")   
    

    
    back2menu()


def updateBook():
    for book_id, book_name in books.items():
            print(f"Book ID: {book_id} - Book Name: {book_name}")
        
    book_id = int(input("Enter the ID of the book to update: "))
    if book_id in books:
        print("Book details:")
        print(f"Book ID: {book_id}")
        print(f"Book Name: {books[book_id]}")

        z= input("Do you want to update this book? (Y/N): ")
        if z == "Y":
            new_book_name = input("Enter the new name for the book: ")
            books[book_id] = new_book_name
            print("Book updated successfully.")
        else:
            print("Book not updated.")
    else:
        print("Invalid book ID.")
    
        lanjut=input("Apa ingin lanjut update(Y/N):")
        
        if lanjut=="Y":
            updateBook()
        elif lanjut=="N":
            back2menu()
    
    back2menu()
    
    
def deleteBook():
    for book_id, book_name in books.items():
        print(f"Book ID: {book_id} - Book Name: {book_name}")
        
    book_id = int(input("Enter the ID of the book to delete: "))
    if book_id in books:
        print("Book details:")
        print(f"Book ID: {book_id}")
        print(f"Book Name: {books[book_id]}")

        choice = input("Do you want to delete this book? (Y/N): ")
        if choice.upper() == "Y":
            removed_book = books.pop(book_id)
            print(f"Book '{removed_book}' removed successfully.")
        else:
            print("Book not deleted.")
    else:
        print("\nInvalid book ID ,Please Insert the Right Id")
        deleteBook()
        
    back2menu()
    

def good2time():
    import webbrowser
    youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(youtube_link)
    print("U got rickrolled!")
    back2menu()
       
    
    
def menu():
    print("\nWelcome to Perpustakaan Joestar!")
    print("1. View Books")
    print("2. Add Book")
    print("3. Update Books")
    print("4. Delete Books")
    print("5. Exit Program")
    print("6. Goodtime :)")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("View Books")
        view()
    elif choice == "2":
       print("\n Add Book ")
       addBook()
    elif choice == "3":
        print("Update Book.")
        updateBook()
    elif choice =="4":
        print("Delete Book")
        deleteBook()
    elif choice == "5":
        print("Exiting the program.")
        return
    elif choice=="6":
        good2time()        
    else:
     print("Invalid choice. Please try again.")   
     menu()

def turnOnDups():
    global allow_duplicates
    allow_duplicates = not allow_duplicates
    status = "enabled" if allow_duplicates else "disabled"
    print(f"Duplicate books are now {status}.")

def back2menu():
    print("\n kembali ke menu utama?")
    x=input("y/n : ")
    if x=="y":
        menu()
    elif x=="n":
        print("Byeee!!")
        return
    else:
        print("Error!")

menu()


































































