from django.test import TestCase, RequestFactory
from django.core import mail
from .models import Book

class TestBookModel(TestCase):
    """
    """
    def setUp(self):
        """
        """
        Book.objects.create(title="Feed the Cat", author="She\'s hangry.", year=2000)
        Book.objects.create(title="Get the Groceries", author="We have none.", year=1994)
        Book.objects.create(title="Art of Diper Change", author="It's stanky.", year=2020 , status="checked-out")

    def test_book_titles(self):
        """
        """
        one = Book.objects.get(title="Feed the Cat")
        self.assertEqual(one.title, "Feed the Cat")

    def test_book_descriptions(self):
        """
        """
        books = Book.objects.all()
        self.assertEqual(books[1].author, "We have none.")

    def test_book_descriptions2(self):
        """
        """
        one = Book.objects.get(title="Art of Diper Change")
        self.assertEqual(one.status, "checked-out")

    def test_create_new_book(self):
        """
        """
        new_book = Book.objects.create(title="New", detail="", year=1998)
        self.assertEqual(new_book.title, "New")
        # pass


class TestBookViews(TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.request = RequestFactory()
        self.note = Book.objects.create(title="Feed the Cat", author="She\'s hangry.", year=2000)
        self.note1 = Book.objects.create(title="Get the Groceries", author="We have none.", year=1994)
        Book.objects.create(title="Art of Diper Change", author="It's stanky.", year=2020 , status="checked-out")

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
        from .views import book_list_view
        request = self.request.get('')
        response = book_list_view(request)
        self.assertEqual(200, response.status_code)        

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