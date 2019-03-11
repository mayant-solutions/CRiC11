from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from pycricbuzz import Cricbuzz
from .models import ScoreCard
from datetime import datetime
c = Cricbuzz()

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/2')), name="some_task", ignore_result=True)
def task_save_live():
    a = c.matches()
    for i in a:
        t = i['start_time'][:10]
        temp_date = datetime.strptime(t, "%Y-%m-%d").date()

        if i['id'] not in ScoreCard.objects.all().values_list('id', flat=True):
            s = ScoreCard()
        else:
            s = ScoreCard.objects.get(ids=i['id'])
        try:
            live = c.livescore(i['id'])
            s.id = i['id']
            logger.info(i['id'])
            s.batrun = live['batting']['score'][0]['runs']
            s.batovers = live['batting']['score'][0]['overs']
            s.batteam = live['batting']['team']
            s.batwickets = live['batting']['score'][0]['wickets']
            s.ballrun = live['bowling']['score'][0]['runs']
            s.ballovers = live['bowling']['score'][0]['overs']
            s.ballteam = live['bowling']['team']
            s.ballwicket = live['bowling']['score'][0]['wickets']

            s.date = temp_date
            s.mchstate = i['status']
            s.save()
        except:
            continue



