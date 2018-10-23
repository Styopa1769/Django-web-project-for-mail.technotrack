"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from core.views import index
from django.contrib.auth import views as auth_views
from core import views as core_views
from django.conf import settings
from django.contrib.staticfiles import views


urlpatterns = [

    url(r'^core/login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'core/logout.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^profile/', include('profiles.urls', namespace='profiles'), name='profiles'),
    url(r'^places/', include('places.urls', namespace='places')),
    url(r'^likes/', include('likes.urls', namespace='likes')),
    url(r'api/', include('api.urls',namespace='api')),
    url(r'',include('social_django.urls'))

]



if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]