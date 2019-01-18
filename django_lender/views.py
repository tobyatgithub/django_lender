from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    """
    Here we define our home view. 
    """
    return render(request, 'generic/home.html', {'message': 'I know you are a Book Lover!'})
