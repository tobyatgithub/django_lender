from django.test import TestCase, RequestFactory
from .models import Book


class TestBookModel(TestCase):
    """
    """
    def setUp(self):
        """
        """
        Book.objects.create(title="Feed the Cat", detail="She\'s hangry.")
        Book.objects.create(title="Get the Groceries", detail="We have none.")
        Book.objects.create(title="Art of Diper Change", detail="It's stanky.", status="In Stock")

    def test_book_titles(self):
        """
        """
        one = Book.objects.get(title="Feed the Cat")
        self.assertEqual(one.title, "Feed the Cat")

    def test_book_descriptions(self):
        """
        """
        books = Book.objects.all()
        self.assertEqual(books[1].detail, "We have none.")

    def test_book_descriptions2(self):
        """
        """
        one = Book.objects.get(title="Art of Diper Change")
        self.assertEqual(one.status, "In Stock")

    def test_create_new_book(self):
        """
        """
        new_book = Book.objects.create(title="New", detail="")
        self.assertEqual(new_book.title, "New")
        # pass


class TestBookViews(TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.request = RequestFactory()
        self.note = Book.objects.create(title="Feed the Cat", detail="She\'s hangry.")
        self.note1 = Book.objects.create(title="Get the Groceries", detail="We have none.")
        Book.objects.create(title="Art of Diper Change", detail="It's stanky.", status="In Stock")

    def test_list_view_contest(self):
        """
        """
        from .views import book_list_view

        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(b'Feed the Cat', response.content)

    def test_list_view_status(self):
        """
        """
        from .view import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertIn(200, response.status_code)        

    def test_detail_view_content(self):
        """
        """
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, primary_key=self.note.id)
        self.assertIn(b'hangry', response.content)

    def test_detail_view_status_code_failure(self):
        """
        """
        from .views import book_detail_view
        from django.http import Http404
        request = self.request.get('')
        with self.assertRaises(Http404):
            book_detail_view(request, '0')