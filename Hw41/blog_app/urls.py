from django.urls import path
from .views import index, post_by_slug

urlpatterns = [
    path('', index),
    path('post/<slug:post_slug>', post_by_slug, name='post_by_slug ')
]
