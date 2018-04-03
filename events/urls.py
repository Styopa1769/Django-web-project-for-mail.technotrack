from django.conf.urls import url
from django.contrib import admin
from core.views import index
from events.views import events_list, event_edit, event_create, event_detail

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        event_detail,
        name="event_detail"
    ),
    url(r'^$', events_list, name="events_list"),
    url(
        r'^edit/(?P<pk>\d+)/$',
        event_edit,
        name="event_edit"
    ),
    url(r'^create/$', event_create, name="event_create")
]