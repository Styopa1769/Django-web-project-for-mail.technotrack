from django.conf.urls import url
from django.contrib import admin
from core.views import index
from places.views import place_detail
from places.views import places_list

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        place_detail,
        name="place_detail"
    ),
    url(r'^$', places_list, name="places_list"),
]