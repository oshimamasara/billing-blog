from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    #text = models.TextField()
    text = MarkdownxField()
    price = models.IntegerField(null=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.text)

    def get_absolute_url(self):
        return reverse('post:post_detail',
                   args=[str(self.slug)])

# to save slug
def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)

class Sell(models.Model):  # Sellsにすると管理画面で Sellss と s が 2つになる
    sold_blog = models.CharField(blank=False, null=False, max_length=100)
    customer_mail = models.CharField(blank=False, null=False, max_length=100)
    Date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True)