from django.urls import path
from . import views

app_name = 'CRiC11'
urlpatterns = [
    path('Player/', views.IndexView.as_view(), name="Playerlist"),
    path('cric11/<int:pk>/', views.DetailView1.as_view(), name="PlayerDetail"),
    path('signup/', views.registrations,name="Registrations"),
    path('create/', views.create, name="Create"),

]
