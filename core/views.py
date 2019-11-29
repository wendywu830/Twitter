from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import Tweet, Hashtag

# Create your views here.
#renders splash & login page
def splash(request):
  return render(request, "splash.html", {})

#renders home page with tweet feed and hashtags
def home(request):
  hashtags_content = []
  tweets = []
  if request.user.is_authenticated:
    #gets up to 15 unique hashtags for display 
    for h in Hashtag.objects.all():
      if (len(hashtags_content) == 15):
        break
      elif(h.content not in hashtags_content):
        hashtags_content.append(h.content)

    # get top 10 most recent tweets
    tweets = Tweet.objects.order_by('-date')[:9]  
    tweet_tuples = []
    for t in tweets:
      tweet_tuples.append((t, t.likes.count()))
    return render(request, "home.html", {"tweet_tuples": tweet_tuples, "hashtags": hashtags_content, "user": request.user})
  else:
    return redirect('/')

#renders profile for user with that id
def profile(request, id):
  tweets = []
  user = None
  if request.user.is_authenticated:
    tweets = Tweet.objects.order_by('-date').filter(author=id)
    tweet_tuples = []
    for t in tweets:
      tweet_tuples.append((t, t.likes.count()))
    user = User.objects.get(id=id)
    return render(request, "profile.html",{"tweet_tuples": tweet_tuples, "user": user})
  else:
    return redirect('/')

#renders sign up page
def signup(request):
  if request.method == "POST":
    user = User.objects.create_user(email=request.POST['email'], username=request.POST['username'], password=request.POST['password'])
    login(request, user)
    return redirect('/home')
  return render(request, "signup.html", {})

def hashtag(request, tag):
  if request.user.is_authenticated:
    hashtag_instances = Hashtag.objects.filter(content=tag) #get all Hashtag obj with diff tweets & same hashtag
    tweets = [h.tweet for h in hashtag_instances]
    tweet_tuples = []
    for t in tweets:
      tweet_tuples.append((t, t.likes.count()))
    return render(request, "hashtag.html", {"hashtag": hashtag_instances[0], "tweet_tuples": tweet_tuples})
  else:
    return redirect('/')

#updates likes for tweet in DB and redirects  
def like(request):
  if request.user.is_authenticated and request.method == "POST":
    user = request.user
    l_id = request.POST["like_id"]
    tweet = Tweet.objects.get(id=l_id)
    if tweet.likes.filter(id=user.id).exists():
      tweet.likes.remove(user)
    else:
      tweet.likes.add(user)
    return redirect('/home')
  else:
    return redirect('/')

#adds tweet in DB and redirects  
def add_tweet(request):
  if request.method == "POST":
    content = request.POST["content"]
    new_tweet = Tweet.objects.create(content=content, author=request.user)
    tags = [c[1:] for c in content.split() if c.startswith("#") and len(c) > 1] # just '#' does not qualify as hashtag
    for t in tags:
      Hashtag.objects.create(tweet=new_tweet, content=t)
  return redirect('/home')

#deletes likes for tweet in DB and redirects  
def delete_tweet(request):
  tweet = Tweet.objects.get(id=request.GET['id'])
  tweet.delete()
  return redirect('/home')

#validates login and redirects 
def login_view(request):
  if request.method == "POST":
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      login(request, user)
      return redirect('/home')
  return redirect('/')

#log out and redirect to login/splash page
def logout_view(request):
  logout(request)
  return redirect("/")