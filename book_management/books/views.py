# books/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


# API endpoint for listing and creating books.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# API endpoint fo retrieving, updating and deleting books
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# API endpoint for checking the availability of a book
@api_view(['GET'])
def check_availability(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        return Response({'available': book.availability})
    except Book.DoesNotExist:
        return Response({'error': 'Book not Found'}, status=status.HTTP_404_NOT_FOUND)


# API endpoint for ordering a book
@api_view(['POST'])
def order_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)

        if book.availability:
            # Book is available, mark it as ordered
            book.availability = False
            book.save()

            return Response({'message': 'Book ordered successfully'})
        else:
            return Response({'error': 'Book is not available for ordering'}, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)






