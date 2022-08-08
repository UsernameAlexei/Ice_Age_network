from django.test import TestCase, Client
from django.urls import reverse
from ice_age.models import Profile, Posts
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        # авторизация для теста
        user = User.objects.create(username='testuser', id=1)
        user.set_password('12345')
        user.save()

        self.client = Client()
        self.logged_in = self.client.login(username='testuser', password='12345')

        # создание поста для теста
        self.test_post = Posts.objects.create(user=user, title='test_title', body='test_body', id=1)
        self.test_delete_post = Posts.objects.create(user=user, title='test_title', body='test_body', id=2)

        # urls для теста
        self.edit_post = reverse('ice_age:edit_post', args=[1])
        self.dashboard_url = reverse('ice_age:dashboard')
        self.delete_post = reverse('ice_age:delete_post', args=[2])
        self.profile_list = reverse('ice_age:profile_list')
        self.profile = reverse('ice_age:profile', args=[1])

    def test_dashboard_GET(self):
        response = self.client.get(self.dashboard_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ice_age/dashboard.html')

    def test_edit_post_GET(self):
        response = self.client.get(self.edit_post)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ice_age/edit_post.html')

    def test_edit_post_POST(self):
        response = self.client.post(self.edit_post, {'title': 'New_test_title', 'body': 'New_test_body'})

        self.test_post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.test_post.title, 'New_test_title')
        self.assertEqual(self.test_post.body, 'New_test_body')

    def test_delete_post_POST(self):
        response = self.client.delete(self.delete_post)

        status_delete = False
        try:
            delete_post = Posts.objects.get(id=2)
        except Posts.DoesNotExist:
            status_delete = True

        self.assertTrue(status_delete)

    def test_profile_list_GET(self):
        response = self.client.get(self.profile_list)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ice_age/profile_list.html')


    # def test_profile_GET(self):
    #     response = self.client.get(self.profile)

        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'ice_age/profile.html')