from django.contrib import admin

# Register your models here.
from .models import Player,Bat,Ball
admin.site.register(Player)
admin.site.register(Bat)
admin.site.register(Ball)
