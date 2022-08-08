from .models import News
from django.core import management
from django.views.generic import ListView


class NewsList(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = 'news_result'

    def get_queryset(self):
        management.call_command('scrape')
        news = News.objects.all().order_by("-created_date")
        return news

