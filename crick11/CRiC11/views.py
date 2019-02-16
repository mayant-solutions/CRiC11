from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Player, Matches
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from pycricbuzz import Cricbuzz


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
    c = Cricbuzz()
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
    c = Cricbuzz()
    return c.livescore(x)


def getdetail(x):
    c=Cricbuzz()

@login_required
def livescore(request):
    c = Cricbuzz()
    a = c.matches()
    li = a[:4]
    id1 = list(map(extract, li))
    sc = list(map(getdata, id1))



    return render(request, 'live.html', {'data': sc})


'''def team(x):
    m.team1 = x['team1']
    m.team2 = x['team2']
    m.bench1 = x['bench1']
    m.bench2 = x['bench2']'''
