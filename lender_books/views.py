from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Book


def book_detail_view(request, primary_key=None):
    """
    """
    context = {
        # 'book': Book.query.get(primary_key)
        'book': get_object_or_404(Book, id=primary_key)
    }
    return render(request, 'books/book_detail.html', context)


def book_list_view(request):
    """
    """
    context = {
        # 'books': Book.query.all()
        'books': get_list_or_404(Book)
    }
    return render(request, 'books/book_list.html', context)    

