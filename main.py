print("Welcome to Book Manager")

books = [
    "The Alchemist",
    "Clean Code",
    "The Art of Programming",
    "History and Evolution of Programming languages",
    "The life of Guido van Rossum"
]

def main():
    display_books()

def add_book():
    book_name = input("Enter the book name you want to add: ")
    if book_name:
        books.append(book_name)
        print(f"Book '{book_name}' has been added successfully")
    else:
        print("Book name cannot be empty")

def remove_book():
    book_name = input("Enter the book name you want to remove: ")
    if book_name in books:
        books.remove(book_name)
        print(f"Book '{book_name}' has been removed successfully")
    else:
        print(f"Book '{book_name}' not found")

def search_book():
    book_name = input("Enter the book name you want to search: ")
    if not book_name:
        print("Book name cannot be empty")
        return
    if book_name in books:
        print(f"Book '{book_name}' has been found successfully")
    else:
        print(f"Book '{book_name}' not found")

def update_book():
    book_name = input("Enter the book name you want to update: ")
    if not book_name:
        print("Book name cannot be empty")
        return
    if book_name in books:
        new_book_name = input("Enter the new book name: ")
        idx = books.index(book_name)
        books[idx] = new_book_name
        print(f"Book '{book_name}' has been updated to '{new_book_name}' successfully")
    else:
        print(f"Book '{book_name}' not found")

def display_books():
    print("Displaying all books:")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book}")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Update Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            display_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            remove_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()