from django.db import models
# from django.utils import timezone
# from django.dispatch import receiver
# from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    """
    """
    cover_image = models.ImageField(upload_to='media', default='no-img.jpg')
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=50)
    detail = models.CharField(max_length=128)
    year = models.IntegerField()

    STATES = [
        ('A', 'available'),
        ('O', 'checked-out'),
    ]
    status = models.CharField(max_length=50, default='available', choices=STATES)
    date_added = models.DateField(auto_now_add=True)
    last_borrowed = models.DateField(auto_now=True)

    def __repr__(self):
        return f'{self.title} ({self.author})'

    def __str__(self):
        return f'{self.title} ({self.author})'

# @receiver(models.signals.post_save, sender=Book)
# def set_book_returned_date(sender, instance, **kwargs):