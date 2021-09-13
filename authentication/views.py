from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django import forms
from tweet.models import Tweet
from authentication.forms import LoginForm, SignUpForm
from twitteruser.models import TwitterUser


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = TwitterUser.objects.create_user(
                username=data['username'], password=data['password'])
        return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'generic_form.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                context = {}
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    context = {'form': form}
    return render(request, 'login_view.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect(reverse('home'))