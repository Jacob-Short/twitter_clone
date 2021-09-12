from django.shortcuts import render,HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import CreateTweetForm
from twitteruser.models import MyUser
import re

@login_required(login_url='/login/')
def index_view(request):


    # tweets from the logged in user
    # user = request.user
    # user_tweets = Tweet.objects.filter(user=user)


    # all the tweets
    # tweets = Tweet.objects.all().order_by('-id')


    context = {}
    return render(request, 'index.html', context)