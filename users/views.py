from django.shortcuts import render
from .models import CustomUser

def profile_view(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'users/profile.html', {'user': user})
