from django.db import models


# Create your models here.
class BatType(models.Model):
    M = models.IntegerField("Matches", null=True)
    Inn = models.IntegerField("Innings", null=True)
    NO = models.IntegerField("Not out", null=True)
    Runs = models.IntegerField("Runs", null=True)
    HS = models.IntegerField("High Score", null=True)
    Avg = models.FloatField("Average", null=True)
    BF = models.IntegerField("Balls Faced", null=True)
    SR = models.FloatField("Strike Rate", null=True)
    century = models.IntegerField("Century", null=True)
    double = models.IntegerField("Double Century", null=True)
    fifty = models.IntegerField("Fifty", null=True)
    fours = models.IntegerField("Fours", null=True)
    sixes = models.IntegerField("Sixes", null=True)


class BallType(models.Model):
    M = models.IntegerField("Matches", null=True)
    Inn = models.IntegerField("Innings", null=True)
    B = models.IntegerField("Balls", null=True)
    Runs = models.IntegerField("Runs", null=True)
    Wkts = models.IntegerField("Wickets", null=True)
    BBI = models.CharField("Best Bowling", max_length=8, null=True)
    BBM = models.CharField("Best Bowling Match", max_length=8, null=True)
    Econ = models.FloatField("Economy", null=True)
    Avg = models.FloatField("Average", null=True)
    SR = models.FloatField("Strike Rate", null=True)
    fwh = models.IntegerField("Fife wicket", null=True)
    twh = models.IntegerField("Ten wicket", null=True)


class Bat(models.Model):
    odibat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='odiba',null=True)
    testbat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='testba',null=True)
    ttbat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='ttba',null=True)
    iplbat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='iplba',null=True)


class Bowl(models.Model):
    odiball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='odib',null=True)
    testball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='testb',null=True)
    ttball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='ttb',null=True)
    iplball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='iplb',null=True)


class Player(models.Model):
    Bat = models.OneToOneField(Bat, on_delete=models.PROTECT, null=True)
    Ball = models.OneToOneField(Bowl, on_delete=models.PROTECT, null=True)
    name = models.CharField("NAME", max_length=20, null=True)
    born = models.DateField("Born", max_length=15, null=True)
    birth = models.CharField("Birth Place", max_length=15, null=True)
    role = models.CharField("Role", max_length=15, null=True)
    batstyle = models.CharField("Bat Style", max_length=15, null=True)
    ballstyle = models.CharField("Ball Style", max_length=15, null=True)

