from django.shortcuts import render, reverse
from django.views import generic
from .models import Player
from django.contrib.auth.mixins import LoginRequiredMixin
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
