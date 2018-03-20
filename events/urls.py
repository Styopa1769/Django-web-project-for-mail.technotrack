from django.conf.urls import url
from django.contrib import admin
from core.views import index
from events.views import event_detail
from events.views import events_list

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        event_detail,
        name="event_detail"
    ),
    url(r'^$', events_list, name="events_list"),
]