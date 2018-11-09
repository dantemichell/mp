from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import get_object_or_404

def logOut(request): 
    logout(request) 
    return redirect('/')