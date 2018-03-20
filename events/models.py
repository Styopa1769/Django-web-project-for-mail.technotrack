# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name