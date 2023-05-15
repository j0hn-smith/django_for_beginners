from django.test import TestCase
from django.urls import reverse

from posts.models import Post


# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("posts:home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("posts:home"))
        self.assertTemplateUsed(response, "posts/post_list.html")

    def test_template_conntent(self):
        response = self.client.get(reverse("posts:home"))
        self.assertContains(response, "This is a test!")
