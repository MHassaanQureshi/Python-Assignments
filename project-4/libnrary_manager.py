books = []

def add_book():
    book_detail = {
        "Title": input("Enter book title: "),
        "Author": input("Enter book author: "),
        "Publication Year": int(input("Enter publication year: ")),  
        "Genre": input("Enter book genre: "),
        "Read status": input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    }
    
    books.append(book_detail)
    print("\nBook added successfully!\n")

def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in books:
        if book["Title"].lower() == title.lower():
            books.remove(book)
            print("\n Book removed successfully!\n")
            return
    print("\n Book not found!\n")

def see_all_books():
    if not books:
        print("\n No books in the collection.\n")
        return
    print("\n List of Books:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Publication Year']}) - {'Read' if book['Read status'] else 'Not Read'}")

def search_book():
    title = input("Enter the book title to search: ").strip()
    found_books = [book for book in books if title.lower() in book["Title"].lower()]
    
    if not found_books:
        print("\n No matching books found.\n")
        return

    print("\n Search Results:")
    for book in found_books:
        print(f"{book['Title']} by {book['Author']} ({book['Publication Year']}) - {'Read' if book['Read status'] else 'Not Read'}")

def display_statistics():
    total_books = len(books)
    if total_books == 0:
        print("\n No books available for statistics.\n")
        return
    
    read_books = sum(1 for book in books if book["Read status"])
    read_percentage = (read_books / total_books) * 100

    print(f"\n Statistics:")
    print(f" Total Books: {total_books}")
    print(f" Books Read: {read_books} ({read_percentage:.2f}%)")

while True:
    print("\n Book Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. See All Books")
    print("4. Search Book")
    print("5. Display Statistics")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        see_all_books()
    elif choice == "4":
        search_book()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        print("\n Exiting program. Goodbye!")
        break
    else:
        print("\n Invalid choice! Please select a valid option.")
