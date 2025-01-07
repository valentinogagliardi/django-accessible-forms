from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from books.models import Book
from books.forms import BookForm


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("")
