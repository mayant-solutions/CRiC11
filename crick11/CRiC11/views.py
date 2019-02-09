from django.shortcuts import render, reverse, redirect
from django.views import generic
from .models import Player
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
            return render(request,'registration/signup.html', {'form':f})
    else:
        f = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': f})
