from celery import shared_task
import time
from NewsPaper.news.models import Post

@shared_task()
def news():
    last_news = Post.objects.all().order_by('time')
    