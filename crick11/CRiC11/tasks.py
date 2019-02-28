from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from .models import Teams

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='*/2')), name="some_task", ignore_result=True)
def task_save_latest_flickr_image():
    a = ['india', 'aus', 'bangladesh', 'south africa', 'pakistan']
    for i in a:
        a = Teams()
        a.name = i
        a.save()
        logger.info('created'+i)