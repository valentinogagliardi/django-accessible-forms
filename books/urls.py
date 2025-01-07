from django.urls import path
from books import views

app_name = "books"

urlpatterns = [
    path("create/", views.BookCreateView.as_view(), name="book-create"),
]
