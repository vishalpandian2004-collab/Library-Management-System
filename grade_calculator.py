
# Library Management System

# Display Book Details
print("===== LIBRARY MANAGEMENT SYSTEM =====")

book_name = "Python Programming"
author = "Guido van Rossum"
price = 450

print("\nBook Details")
print("Book Name :", book_name)
print("Author    :", author)
print("Price     : Rs.", price)


# Book Issue Functionality
def issue_book():
    print("\n===== BOOK ISSUE DETAILS =====")

    student_name = input("Enter Student Name: ")
    book = input("Enter Book Name: ")

    print("\nBook Issued Successfully!")
    print("Student Name :", student_name)
    print("Book Name    :", book)


# Call the function
issue_book()
