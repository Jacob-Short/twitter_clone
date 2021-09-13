from django.shortcuts import render,HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import CreateTweetForm
from twitteruser.models import TwitterUser
import re

@login_required(login_url='/login/')
def index_view(request):


    # tweets from the logged in user
    # user = request.user
    # user_tweets = Tweet.objects.filter(user=user)


    # all the tweets
    tweets = Tweet.objects.all().order_by('-id')


    context = {'tweets': tweets}
    return render(request, 'index.html', context)


@login_required
def create_tweet_view(request):
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                body=data['body'],
                user=request.user,
            )
            return HttpResponseRedirect(reverse('home'))
    form = CreateTweetForm()
    context = {'form': form}
    return render(request, 'generic_form.html', context)


def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    context = {'tweet': tweet}
    return render(request, 'tweet_detail.html', context)