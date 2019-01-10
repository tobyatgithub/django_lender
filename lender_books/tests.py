from .models import Book
from django.core import mail
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory


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
    Here we mainly test book views which requires user login.
    """

    def setUp(self):
        """
        First we set up some objects to run before every following test methods.
        Notice that I grabbed username and password from the django document,
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
        """

        # create two users
        self.test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        self.test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        self.test_user1.save()
        self.test_user2.save()

        self.request = RequestFactory()
        self.note = Book.objects.create(title="Feed the Cat", author="She\'s hangry.", year=2000)
        self.note1 = Book.objects.create(title="Get the Groceries", author="We have none.", year=1994)
        Book.objects.create(title="Art of Diper Change", author="It's stanky.", year=2020 , status="checked-out")

    def test_home_view_contest(self):
        """
        Test logined in user getting into home page
        """
        from .views import book_list_view
        # login
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('')
        # import pdb; pdb.set_trace()
        self.assertIn(b'Greetings Book Lovers!', response.content)

    def test_book_list_view_contest(self):
        """
        Test logined in user getting into home page
        """
        from .views import book_list_view
        # login
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse(book_list_view))
        # import pdb; pdb.set_trace()
        self.assertIn(b'<title>Book List Page - Books!</title>\n', response.content)

    def test_book_detail_view_status(self):
        """
        """
        from .views import book_detail_view
        # login
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse(book_detail_view, kwargs={'primary_key': self.note.id}))
        # import pdb; pdb.set_trace()
        self.assertEqual(200, response.status_code)  
        self.assertIn(b'<p> Year: 2000</p>\n', response.content)

    def test_detail_view_status_code_failure(self):
        """
        """
        from .views import book_detail_view
        from django.http import Http404
        # acquire detailed book page without login.
        response = self.client.get(reverse(book_detail_view, kwargs={'primary_key': self.note.id}))
        self.assertEqual(302, response.status_code)