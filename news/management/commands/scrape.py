from django.core.management.base import BaseCommand

from urllib.request import urlopen
from bs4 import BeautifulSoup
from news.models import News


class Command(BaseCommand):
    help = "collect news"

    # определяем логику команд
    def handle(self, *args, **options):

        # собираем html
        html = urlopen('https://www.sostav.ru/lenta')

        # преобразуем в soup-объект
        soup = BeautifulSoup(html, 'html.parser')

        # собираем все посты
        lenta = soup.find_all('a', class_='title')

        for post in lenta:

            try:
                # сохраняем в базе данных
                News.objects.create(
                    url=f'https://www.sostav.ru{post["href"]}',
                    content=post.text)

                print('%s added' % (post.text,))
            except:
                print('%s already exists' % (post.text,))

        self.stdout.write('news complete')
