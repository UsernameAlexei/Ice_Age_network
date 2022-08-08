from django.test import SimpleTestCase
from ice_age.forms import PostsForm


class TestForm(SimpleTestCase):

    def test_posts_form_is_valid(self):
        form = PostsForm(data={
            'title': 'test_title',
            'body': ' test_body'
        })

        self.assertTrue(form.is_valid())

    def test_posts_form_no_data(self):
        form = PostsForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
