from django.contrib import admin

# Register your models here.
from .models import Player, Bat, Bowl, BallType, BatType,Matches,ScoreCard, Teams

admin.site.register(Player)
admin.site.register(Bat)
admin.site.register(Bowl)
admin.site.register(BallType)
admin.site.register(BatType)
admin.site.register(Matches)
admin.site.register(ScoreCard)
admin.site.register(Teams)