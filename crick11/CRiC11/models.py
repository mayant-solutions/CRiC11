from django.db import models


# Create your models here.
class Bat(models.Model):
    M = models.IntegerField("Matches", max_length=20)
    Inn = models.IntegerField("Innings", max_length=20)
    NO = models.IntegerField("Not out", max_length=20)
    Runs = models.IntegerField("Runs", max_length=20)
    HS = models.IntegerField("High Score", max_length=20)
    Avg = models.IntegerField("Average", max_length=20)
    BF = models.IntegerField("Balls Faced", max_length=20)
    SR = models.IntegerField("Strike Rate", max_length=20)
    century = models.IntegerField("Century", max_length=20)
    double = models.IntegerField("Double Century", max_length=20)
    fifty = models.IntegerField("Fifty", max_length=20)
    fours = models.IntegerField("Fours", max_length=20)
    sixes = models.IntegerField("Sixes", max_length=20)


class Ball(models.Model):
    M = models.IntegerField("Matches", max_length=20)
    Inn = models.IntegerField("Innings", max_length=20)
    B = models.IntegerField("Balls", max_length=20)
    Runs = models.IntegerField("Runs", max_length=20)
    Wkts = models.IntegerField("Wickets", max_length=20)
    BBI = models.IntegerField("Best Bowling", max_length=20)
    BBM = models.IntegerField("Best Bowling Match", max_length=20)
    Econ = models.IntegerField("Economy", max_length=20)
    Avg = models.IntegerField("Average", max_length=20)
    SR = models.IntegerField("Strike Rate", max_length=20)
    fwh = models.IntegerField("Fife wicket", max_length=20)
    twh = models.IntegerField("Ten wicket", max_length=20)


class Player(models.Model):
    p = models.OneToOneField(Bat, on_delete=models.PROTECT)
    p = models.OneToOneField(Ball, on_delete=models.PROTECT)
    name = models.CharField("NAME", max_length=200)
    born = models.IntegerField("Matches", max_length=20)
    birth = models.IntegerField("Matches", max_length=20)
    role = models.IntegerField("Matches", max_length=20)
    batstyle = models.IntegerField("Matches", max_length=20)
    ballstyle = models.IntegerField("Matches", max_length=20)


