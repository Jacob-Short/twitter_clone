from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django import forms
from tweet.models import Tweet
from twitteruser.models import TwitterUser

def user_detail(request, id):
    user = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(user=user)
    users_page = user
    tweets_count = 0
    for _ in tweets:
        tweets_count += 1
    context = {'tweets': tweets, 'tweets_count': tweets_count, 'users_page': users_page}
    return render(request, 'user_detail.html', context)
