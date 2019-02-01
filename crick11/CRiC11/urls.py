from django.urls import path
from .import views
urlpatterns = [
    path('Player/',views.IndexView.as_view,name="Playerlist"),
    path('cric11/',views.DetailView.as_view,name="PlayerDetail"),
]