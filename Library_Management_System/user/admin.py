from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn','title','author','publication_date','genre','availability','num_available']
