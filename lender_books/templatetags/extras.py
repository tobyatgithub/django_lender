from django.utils import timezone
from django import template

# register our function into the template by 
# 1. calling the library, and 2. register
register = template.Library()


@register.filter
def get_date_string(value):
    """
    """
    now_aware = timezone.now()
    delta = now_aware - value

    if delta.days == 0:
        return 'Today!'
    elif delta.days < 0:
        return 'Tomorrow'
    elif delta.days > 0:
        return f'Added { delta.days } days ago'