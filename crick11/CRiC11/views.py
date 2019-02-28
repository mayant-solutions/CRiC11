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
from celery.schedules import crontab
from celery.task import periodic_task
from .models import ScoreCard
import bs4
import requests

c = Cricbuzz()
newsapi = NewsApiClient(api_key='b96cfe4919f6490c97cacf7961f31ca0')
from .forms import NameForm


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
    if c.livescore(x):

        return True
    else:
        return False


def getsome(x):
    return c.livescore(x)


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
    try:

        sc = list(filter(getdata, id1))
        sc = list(map(getsome, sc))
    except:
        sc = []

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


@periodic_task(run_every=crontab(hour=0, minute=1, day_of_week="mon,tue,wed,thu,fri,sat,sun"))
def every():
    s = ScoreCard()
    a = c.matches()
    li = []
    for i in a:
        if i['mchstate'] == 'inprogress':
            li.append(i)

    id1 = list(map(extract, li))
    try:

        sc = list(filter(getdata, id1))
        sc = list(map(getsome, sc))
    except:
        sc = []
    for i in sc:
        s.batteam = i['batting'][0]['team']
        s.runs = i['batting']['score'][0]['runs']
        s.pship = i['patnership']
        s.wickets = i['batting']['score'][0]['wickets']
        s.overs = i['batting']['score'][0]['overs']
        s.run_rate = i['run_rate']
        s.bat1name = i['batting']['batsman'][0]['name']
        s.b1runs = i['batting']['batsman'][0]['runs']
        s.b1ballfaced = i['batting']['batsman'][0]['balls']
        s.b1fours = i['batting']['batsman'][0]['fours']
        s.b1sixes = i['batting']['batsman'][0]['sixes']
        s.bat2name = i['batting']['batsman'][1]['name']
        s.b2runs = i['batting']['batsman'][1]['runs']
        s.b2ballfaced = i['batting']['batsman'][1]['balls']
        s.b2fours = i['batting']['batsman'][1]['fours']
        s.b2sixes = i['batting']['batsman'][1]['sixes']
        s.bowlername = i['bowling']['bowler'][0]['name']
        s.save()


def capital(x):
    return x.capitalize()


def wiki(request):
    def extract(x):
        return x.getText()

    if request.method == 'POST':
        f = NameForm(request.POST)
        if f.is_valid():

            Search = f.cleaned_data.get('search')
            a = Search.split(" ")
            a = list(map(capital, a))
            s = '_'.join(a)
            try:
                rest = requests.get('https://en.wikipedia.org/wiki/' + s)
                rest.raise_for_status()
                a = bs4.BeautifulSoup(rest.text, 'lxml')

                ele = a.select('p')
                out = list(map(extract, ele))
                for i in out[:3]:

                    if ('cricketer' in i):
                        break
                else:
                    out = []

            except:
                out = []

            return render(request, 'CRiC11/playerdetail.html', {'data': out})
        else:
            return render(request, 'CRiC11/player.html', {'form': f})
    else:
        f = NameForm()
        return render(request, 'CRiC11/player.html', {'form': f})


'''def team(x):
    m.team1 = x['team1']
    m.team2 = x['team2']
    m.bench1 = x['bench1']
    m.bench2 = x['bench2']'''
