from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Post


# Create your tests here.
class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@mail.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="A good title", body="Lorem Ipsum", author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Lorem Ipsum")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/blog/post/1/")

    def test_create_post(self):
        response = self.client.post(
            reverse("blog:post_new"),
            {"title": "New Title", "body": "New Text", "author": self.user.id},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New Title")
        self.assertEqual(Post.objects.last().body, "New Text")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("blog:post_edit", args="1"),
            {"title": "Edit Title", "body": "Edit Text"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Edit Title")
        self.assertEqual(Post.objects.last().body, "Edit Text")

    def test_post_deleteview(self):
        self.assertIn(self.post, Post.objects.all())
        response = self.client.post(reverse("blog:post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.post, Post.objects.all())
