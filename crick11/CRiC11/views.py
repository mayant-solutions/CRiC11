from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Player, Matches
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from pycricbuzz import Cricbuzz
from newsapi import NewsApiClient

c = Cricbuzz()
newsapi = NewsApiClient(api_key='b96cfe4919f6490c97cacf7961f31ca0')


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'player'
    template_name = 'Playerlist.html'
    model = Player

    def get_queryset(self):
        return Player.objects.all()


class DetailView1(LoginRequiredMixin, generic.DetailView):
    context_object_name = 'players'
    model = Player
    template_name = 'CRiC11/Players.html'


def registrations(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('CRiC11:Playerlist')
        else:
            return render(request, 'registration/signup.html', {'form': f})
    else:
        f = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': f})


def create(request):
    a = c.matches()
    for i in a:
        m = Matches()
        m.id = i['id']
        m.srs = i['srs']
        m.status = i['status']
        m.type = i['type']
        m.mnum = i['mnum']
        m.venue_name = i['venue_name']
        m.venue_location = i['venue_location']
        m.toss = i['toss']
        m.save()
    return redirect(request, 'live.html', m)


def extract(x):
    return x['id']


def getdata(x):

    try:

        return c.livescore(x)
    except:
        return x


def getdetail(x):
    c = Cricbuzz()


@login_required
def livescore(request):
    a = c.matches()
    li = []
    for i in a:
        if i['mchstate'] == 'inprogress':
            li.append(i)


    id1 = list(map(extract, li))
    sc = list(map(getdata, id1))

    return render(request, 'live.html', {'value': sc})


def home(request):
    return render(request, 'CRiC11/home.html')


def schedule(request):
    b = c.matches()

    def filterr(x):
        if x['mchstate'] == 'preview':
            return x

    y = list(filter(filterr, b))
    return render(request, 'CRiC11/schedule.html', {'list': y})


def news(request):
    top_headlines = newsapi.get_top_headlines(q='cricket', category='sports', language='en')
    hl = top_headlines['articles']
    return render(request, 'CRiC11/news.html', {'news': hl})


'''def team(x):
    m.team1 = x['team1']
    m.team2 = x['team2']
    m.bench1 = x['bench1']
    m.bench2 = x['bench2']'''
