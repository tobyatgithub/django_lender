from django.utils import timezone
from django import template

# register our function into the template by 1. calling the library, and 2. @register
register = template.library()


@register.filter
def get_date_string(value):
    """
    """
    now_aware = timezone.now()
    delta = value - now_aware

    if delta.days == 0:
        return 'Today!'
    elif delta.days == 1:
        return 'Tomorrow'
    elif delta.days > 1:
        return f'In { delta.days } days'