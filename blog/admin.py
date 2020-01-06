from django.contrib import admin
from .models import Post, Sell
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug','price', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

class SellAdmin(admin.ModelAdmin):
    list_display = ('id', 'sold_blog', 'customer_mail', 'Date', 'price')

admin.site.register(Post, PostAdmin)
admin.site.register(Sell, SellAdmin)
#admin.site.register(Post, MarkdownxModelAdmin)