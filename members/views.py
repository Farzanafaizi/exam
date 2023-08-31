from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def Blog_list(request):
    post = Blogpost.object.all()
    return render(request, 'blog_list.html', {'posts' :post})
