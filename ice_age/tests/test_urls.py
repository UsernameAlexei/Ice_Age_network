from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ice_age.views import edit_post, dashboard, DeletePost, ProfileList, profile

class TestUrls(SimpleTestCase):

    def test_url_edit_post(self):
        url = reverse("ice_age:edit_post", args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, edit_post)

    def test_url_dashboard(self):
        url = reverse("ice_age:dashboard")
        # print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard)

    def test_url_delete_post(self):
        url = reverse("ice_age:delete_post", args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DeletePost)

    def test_url_profile_list(self):
        url = reverse("ice_age:profile_list")
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProfileList)

    def test_url_profile(self):
        url = reverse("ice_age:profile", args=[1])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, profile)
