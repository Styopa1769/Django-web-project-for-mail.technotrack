# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from events.models import Event


class Blog(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    events = models.ManyToManyField(Event, blank=True)
