from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('about/', views.about, name='about'),
    #path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/', views.fee_detail, name='fee_detail'),
    path('', views.index, name='index'),
]
