from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Bookmark

# Create your views here.
#A view to display all bookmarks
def bookmark_list(request):
    bookmarks = Bookmark.public.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'marcador/bookmark_list.html', context)

#A view for each user
def bookmark_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        bookmarks = user.bookmarks.all()
    else:
        bookmarks = Bookmark.public.filter(owner__username=username)
    context = {'bookmarks': bookmarks, 'owner': user}
    return render(request, 'marcador/bookmark_user.html', context)
