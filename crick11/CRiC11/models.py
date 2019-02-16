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
    odibat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='odiba', null=True)
    testbat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='testba', null=True)
    ttbat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='ttba', null=True)
    iplbat = models.OneToOneField(BatType, on_delete=models.CASCADE, related_name='iplba', null=True)


class Bowl(models.Model):
    odiball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='odib', null=True)
    testball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='testb', null=True)
    ttball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='ttb', null=True)
    iplball = models.OneToOneField(BallType, on_delete=models.CASCADE, related_name='iplb', null=True)


class Player(models.Model):
    Bat = models.OneToOneField(Bat, on_delete=models.PROTECT, null=True)
    Ball = models.OneToOneField(Bowl, on_delete=models.PROTECT, null=True)
    name = models.CharField("NAME", max_length=20, null=True)
    born = models.DateField("Born", max_length=15, null=True)
    birth = models.CharField("Birth Place", max_length=15, null=True)
    role = models.CharField("Role", max_length=15, null=True)
    batstyle = models.CharField("Bat Style", max_length=15, null=True)
    ballstyle = models.CharField("Ball Style", max_length=15, null=True)
    profile = models.CharField("Ball Style", max_length=30000, null=True)

    def __str__(self):
        return self.name


class Teams(models.Model):
    name = models.CharField("Team", max_length=30)


class Matches(models.Model):
    id = models.CharField("id", max_length=15, primary_key=True)
    srs = models.CharField("Series", max_length=15, null=True)
    mnum = models.CharField("Match number", max_length=15, null=True)
    type = models.CharField("Match type", max_length=15, null=True)
    mchstate = models.CharField("State", max_length=30, null=True)
    status = models.CharField("Status", max_length=30, null=True)
    venue_name = models.CharField("Venue", max_length=30, null=True)
    venue_location = models.CharField("Location", max_length=15, null=True)
    toss = models.CharField("Toss", max_length=15, null=True)
    start_time = models.CharField("Start time", max_length=15, null=True)
    run_rate= models.FloatField("Run Rate", null=True)
    '''team1 = models.ForeignKey(Teams, "Squad1", max_length=375, null=True, related_name='team1')
    bench1 = models.ForeignKey(Teams,"Bench1", max_length=375, null=True, related_name='bench1')
    team2 = models.ForeignKey(Teams,"Squad2", max_length=375, null=True, related_name='team2')
    bench2 = models.ForeignKey(Teams,"Bench2", max_length=375, null=True, related_name='bench2')'''


class ScoreCard(models.Model):
    batteam = models.CharField("Batting", max_length=15, null=True, )
    runs = models.IntegerField("Runs", null=True)
    wickets = models.IntegerField("Partnership", null=True)
    overs = models.FloatField("Overs", null=True)
    inng_num = models.IntegerField("Innings NO", null=True)
    extras = models.IntegerField("Extras", null=True)


class News(models.Model):
    head = models.CharField("Headings", max_length=200, null=True)
    news = models.CharField("News", max_length=50000, null=True)
    teams = models.ForeignKey(Teams, name="Teams", on_delete=models.CASCADE)


