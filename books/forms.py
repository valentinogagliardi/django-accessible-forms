from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            auto_id = self.auto_id % field_name
            field.widget.attrs.update(
                {
                    "aria-describedby": f"{auto_id}_errorlist {auto_id}_helptext",
                }
            )

            # Set initial aria-invalid="false" to avoid screen readers
            # announcing non-touched fields as invalid by default
            if (
                not field.widget.is_hidden
                and field_name not in self.errors
                and field.required
            ):
                field.widget.attrs.update({"aria-invalid": "false"})

    class Meta:
        model = Book
        fields = ["title", "publication_date", "description", "author"]

        labels = { 
            "title": "Title (required)",
            "publication_date": "Publication Date (required)",
            "description": "Description (optional)",
            "author": "Author (required)",
        }

        help_texts = {
            "title": "Enter the title of the book.",
            "publication_date": "Enter the publication date.",
            "author": "Select the author of the book.",
        }
