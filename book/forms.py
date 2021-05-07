from django import forms

from book.models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'ISBN', 'Author']

