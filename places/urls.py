from django.conf.urls import url
from django.contrib import admin
from core.views import index
from places.views import place_detail, place_edit
from places.views import places_list, place_create

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        place_detail,
        name="place_detail"
    ),
    url(r'^$', places_list, name="places_list"),
    url(
        r'^edit/(?P<pk>\d+)/$',
        place_edit,
        name="place_edit"
    ),
    url(r'^create/$', place_create, name="place_create")
]