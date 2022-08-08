from django.test import TestCase, Client
from ice_age.models import Profile, Posts
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self) -> None:
        # авторизация для теста
        user = User.objects.create(username='testuser', id=1)
        user.set_password('12345')
        user.save()

        self.test_post = Posts.objects.create(user=user, title='test_title', body='test_body', id=1)

    def test_posts_is_created(self):
        self.assertEqual(self.test_post.title, 'test_title')
        self.assertEqual(self.test_post.body, 'test_body')