from django.shortcuts import render
from django.views import generic
from .models import Player


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Players/index.html'
    model = Player

    def get_queryset(self):
        return Player.object.all()


class DetailView(generic.DetailView):
    model = Player
    template_name = 'Players/detail.html'
