from django.conf.urls import url
from django.contrib import admin
from core.views import index
from events.views import events_list, EventEdit, EventCreate, event_detail
from events.models import EventForm

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        event_detail,
        name="event_detail"
    ),
    url(r'^$', events_list, name="events_list"),
    url(
        r'^edit/(?P<pk>\d+)/$',
        EventEdit.as_view(),
        name="event_edit"
    ),
    url(r'^create/$', EventCreate.as_view(), name="event_create")
]