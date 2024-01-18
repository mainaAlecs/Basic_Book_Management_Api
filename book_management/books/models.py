from django.db import models


# Model representing a book
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)

    # String representation of the book
    def __str__(self):
        return self.title

