from django.urls import path
from .views import (signup_form,Login,Profile,LogOut,Bookadd,
                    SubmitBook,Home,Showbooks,Book_Search,Book_detail,view_wishlist)
urlpatterns = [
    path('home/',Home,name='HOME'),
    path('signup/',signup_form,name='SIGNUP'),
    path('login/',Login,name='LOGIN'),
    path('profile/',Profile,name='PROFILE'),
    path('logout/',LogOut,name='LOGOUT'),
    path('add_book/',Bookadd,name='ADDBOOK'),
    path('successful/',SubmitBook,name='Donebook'),
    path('showbooks/',Showbooks,name='SHOWBOOK'),
    path('booksearch/',Book_Search,name='BOOKSEARCH'),
    path('bookdetail/<int:isbn>/',Book_detail,name='BOOKDETAIL'),
    path('wishlist/',view_wishlist,name='WISHLIST'),
]
