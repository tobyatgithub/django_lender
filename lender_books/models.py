from django.db import models
# from django.utils import timezone
# from django.dispatch import receiver


class Book(models.Model):
    """
    Here we define how we going to store data in database. 
    These variables also will be the reference for front end (html) pages
    to grab and select.
    """

    # notice that a default value is usually a good idea,
    # otherwise you may need to bash into the container and 
    # mannually setup the database by offereing default value
    # manage.py makemigration --noinput will fail at first deployment.
    cover_image = models.ImageField(upload_to='media', default='no-img.jpg')
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=50)
    detail = models.CharField(max_length=128)
    year = models.IntegerField()

    # choices is expecting a list of tuples.
    STATES = [
        ('A', 'available'),
        ('O', 'checked-out'),
    ]

    status = models.CharField(max_length=50, default='available', choices=STATES)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.title} ({self.author})'

    def __str__(self):
        return f'{self.title} ({self.author})'

# @receiver(models.signals.post_save, sender=Book)
# def set_book_returned_date(sender, instance, **kwargs):