from django.shortcuts import render
from .models import  Post
# Create your views here.
def promos(request):
    posts = Post.objects.all()
    return render(request, "promos/promos.html", {'posts': posts})