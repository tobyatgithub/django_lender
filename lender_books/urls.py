from .views import book_detail_view, book_list_view
from django.urls import path


# connect view controllers and their templates
urlpatterns = [
    path('', book_list_view, name='book_list'), 
    path('<int:primary_key>', book_detail_view, name='book_detail'),
]
