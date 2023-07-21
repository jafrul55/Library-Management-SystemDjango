Library Management System - Django
Welcome to the Library Management System built using Django! This project provides a user-friendly web application to manage a library effectively. 
#Below are the key features of this system:

Home Page: The landing page that introduces the library and its services.

Signup Page: New users can register and create an account to access the library services.

Login Page: Registered users can log in to their accounts securely.

Profile Page: After logging in, users can view their profile information. The profile page also contains a logout option for easy session management.

Add Book Page: Admin users can add new books to the library database, including details such as title, author, genre, and availability status.

Show Book Page: Users can explore the collection of books available in the library. From this page, users can borrow specific books, return books they previously borrowed, and add books to their wishlist.

Wishlist: Each user has their own wishlist, allowing them to save books they are interested in for future reference.

Borrow Book: Users can borrow books from the library. When they borrow a book, its availability status is updated in the database.

Return Book: Once users have finished reading a borrowed book, they can return it, and the availability status is updated accordingly.

Admin Control: The system includes an admin login that allows authorized personnel to manage the library efficiently. Admins can update book information and delete books from the backend.

User Permissions: Admins have the power to grant permission for other users to sign up and use the library application.

Borrowed Book Tracking: The system keeps track of borrowed books, allowing both users and admins to view the borrowing history.

This project aims to simplify the process of managing a library, making it convenient for both users and administrators.
With user authentication and personalized features like wishlists, users can have a tailored experience. Admins have full control over book management and user permissions, ensuring the smooth operation of the library.

#How to Use
1. Setup: Clone the repository and install the necessary dependencies using pip.

2. Database: Configure your database settings in Django's settings.py file and run migrations to create the necessary tables.

3. Admin Access: To access the admin panel, login with the provided admin credentials (username: library, password: 12345).

4. Run the Server: Launch the development server using python manage.py runserver.

5. Home Page: Visit the home page to explore the library's services.

6. Signup: New users can create an account by visiting the signup page.

7. Login: Registered users can log in securely using their credentials.

8. Profile: Once logged in, users can view their profile and log out from the profile page.

9. Adding Books: Admins can add new books to the library from the "Add Book" page.

10. Browsing Books: Users can browse the library collection on the "Show Book" page. They can borrow, return, or add books to their wishlist.

11. Wishlist: Each user has a personal wishlist where they can manage their desired books.

12. Borrowing Books: Users can borrow books they are interested in from the library.

13. Returning Books: Once users finish reading a borrowed book, they can return it.

14. Admin Control: Admins have access to the backend, allowing them to update book info and delete books.

15. User Permissions: Admins can grant permissions to other users to sign up and use the app.

16. Borrowed Book Tracking: The system tracks borrowed books, providing visibility into borrowing history.

We hope you find this Library Management System helpful in efficiently managing your library's resources. 
If you have any feedback or suggestions, feel free to contribute to the project or get in touch with us. Happy Coding!
Md.Jafrul Alam Tusar
