# books/urls.py
from django.urls import path
from .views import BookList, BookDetail, check_availability, order_book

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('check-availability/<int:pk>/', check_availability, name='check-availability'),
    path('order-book/<int:pk>/', order_book, name='order-book'),
]
