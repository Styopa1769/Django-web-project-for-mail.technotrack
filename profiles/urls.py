from django.conf.urls import url
from profiles.views import profile_details

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        profile_details,
        name="profile_details"
    ),
]