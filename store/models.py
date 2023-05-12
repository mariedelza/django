from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CreateBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    intro = models.TextField()
    auteur = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("my-articles")

    class Meta:
        ordering = ['-date_added', '-date_update']


# class Comment(models.Model):
#     post = ForeignKey(CreateBlog, related_name='comments',
#                       on_delete=models.CASCADE)
#     email = models.EmailField()
#     body = models.TextField()
#     name = models.CharField(max_length=200, default="marie")
#     date_added = models.DateTimeField(auto_now=True)
#     date_update = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-date_added', '-date_update']
