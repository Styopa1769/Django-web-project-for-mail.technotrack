# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Event(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='events',
        verbose_name=u'Автор'
    )
    name = models.CharField(max_length=255, verbose_name=u'Имя события')
    is_archive = models.BooleanField(default=False, verbose_name=u'Событие в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'
        ordering = 'name', 'id'


    def __unicode__(self):
        return self.name