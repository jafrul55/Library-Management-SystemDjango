# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta
from .models import BorrowedBook

@shared_task
def check_overdue_books():
    today = datetime.now().date()
    overdue_books = BorrowedBook.objects.filter(due_date__lte=today, returned=False)

    for book in overdue_books:
        # Send a reminder email to the user
        send_mail(
            'Reminder: Overdue Book Return',
            f"Dear {book.user.username},\n\nThis is a reminder that the book '{book.book.title}' is overdue for return. Please return it as soon as possible to avoid fines.\n\nThank you.",
            'library@example.com',
            [book.user.email],
            fail_silently=False,
        )
