from django.shortcuts import render,get_object_or_404,redirect
from .forms import Signup,BookForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Book,Wishlist,BorrowedBook,Fine
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
from django.utils import timezone



#Homepage:
def Home(request):
    return render(request,'Home/home.html')

#SignUp
def signup_form(request):
    if request.method == 'POST':
        frm = Signup(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponseRedirect('/sign/login')
    else:
        frm = Signup()
    return render(request,'user/signup.html',{'form':frm})
    

#Login
def Login(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request,data = request.POST)
        if frm.is_valid():
            userName = frm.cleaned_data['username']
            userPassword = frm.cleaned_data['password']
            user = authenticate(username = userName,password = userPassword)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/sign/profile')
    else:
        frm = AuthenticationForm()
    return render(request,'user/login.html',{'form':frm})
   
@login_required
def Profile(request):
    user = request.user
    return render(request,'user/profile.html',{'User':user})

#LogOut
def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/sign/login')

# Book add
@login_required
def Bookadd(request):
    if request.method == 'POST':
        frm = BookForm(request.POST)
        if frm.is_valid():
            frm.save()
            # notify = 'Book info successful'
            print(frm.cleaned_data)
            return HttpResponseRedirect('/sign/successful')     
    else:
       frm = BookForm()
    return render(request,'book/add_book.html',{'form':frm})
            
#Successfully submit book
@login_required
def SubmitBook(request):
    return render(request,'user/successful.html')

#Show books
@login_required
def Showbooks(request):
    book = Book.objects.all()
    return render(request,'book/show_book.html',{'Show':book})

    def log(self):
        if Showbooks == LogOut:
            return redirect(LOGIN)
        
        
#Book search
@login_required
def Book_Search(request):
    query = request.GET.get('booksearch')
    search_criteria = request.GET.get('search_criteria','title')
    if query:
        if search_criteria == 'isbn':
            books = Book.objects.filter(isbn__icontains = query)
        elif search_criteria == 'author':
            books = Book.objects.filter(author__icontains = query)
        elif search_criteria == 'genre':
            books = Book.objects.filter(genre__icontains = query)
        else:
            books = Book.objects.filter(title__icontains = query)
    else:
        books = []
    # for book in books:
    #     book.fine_amount = calculate_fine(book)
    return render(request,'book/book_search.html',{'books':books})


@login_required
def Book_detail(request,isbn):
    book = get_object_or_404(Book,isbn=isbn)
    borrowed_books = BorrowedBook.objects.filter(user=request.user, book=book, returned=False)
    fine_amount = None
    if borrowed_books:
        # Assuming each user can borrow only one copy of the book at a time
        borrowed_book = borrowed_books.first()  # Get the first borrowed book (if available)

        if borrowed_book.due_date < timezone.now().date():
            days_late = (timezone.now().date() - borrowed_book.due_date).days
            fine_rate = 0.50  # Example: $0.50 fine per day
            max_fine = 10.0  # Example: Maximum fine amount $10.00
            fine_amount = min(days_late * fine_rate, max_fine)
    else:
        fine_amount = None

    #Check if the book is in the user's wishlist
    in_wishlist = Wishlist.objects.filter(user = request.user,book=book).exists()

    if request.method == 'POST':
        if 'borrow' in request.POST:
            if book.num_available > 0:
                BorrowedBook.objects.create(user = request.user,book=book,due_date = datetime.now() + timedelta(days=14))
                book.num_available -= 1
                book.save()
                return redirect('SHOWBOOK')
                
        elif 'return' in request.POST:
            # borrowed_book = BorrowedBook.objects.get(user = request.user,book=book,returned = False)
            for borrowed_book in borrowed_books:
                borrowed_book.returned = True
                borrowed_book.save()
                book.num_available += 1
                book.save()
                return redirect('SHOWBOOK')
                
        elif 'add_to_wishlist' in request.POST:
            if not Wishlist.objects.filter(user=request.user, book=book).exists():
                Wishlist.objects.create(user=request.user, book=book)
                return redirect('WISHLIST')     
    return render(request,'borrow/book_details.html',{'book':book,'borrowed_books':borrowed_books,'fine_amount':fine_amount,'Wishlist':in_wishlist})

        
        
@login_required
def view_wishlist(request):
    if request.method == 'POST':
        if "remove_from_wishlist" in request.POST:
            book_isbn = request.POST.get('remove_from_wishlist')
            book = get_object_or_404(Book,isbn=book_isbn)
            Wishlist.objects.filter(user=request.user,book=book).delete() 
    wishlist_book = Wishlist.objects.filter(user=request.user)
    return render(request, 'borrow/wishlist.html', {'wishlist_books': wishlist_book})



        
        
