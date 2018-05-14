from django.conf.urls import url
from django.contrib import admin
from core.views import index
from likes.views import LikeCreate

urlpatterns = [
    url(r'^create/$', LikeCreate.as_view(), name="like_create")
]