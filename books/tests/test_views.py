import pytest

from unbrowsed import parse_html, get_by_role

@pytest.mark.django_db
def test_book_create(client):
    """Test get request to the book create view."""
    response = client.get("/books/create/")
    dom = parse_html(response.content)
    get_by_role(dom, "textbox", description="Enter the title of the book.")
    assert get_by_role(dom, "form").to_have_attribute("novalidate")

    """Test post request to the book create view."""
    response = client.post(
        "/books/create/",
        {
            "title": "",
        },
    )
    dom = parse_html(response.content)
    get_by_role(dom, "textbox", description="This field is required. Enter the title of the book.")