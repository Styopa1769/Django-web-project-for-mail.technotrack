# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

from events.models import Event


class Blog(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blogs',
        verbose_name=u'Автор'
    )
    name = models.CharField(max_length=255, verbose_name=u'Имя блога')
    is_archive=models.BooleanField(default=False, verbose_name=u'Блог в архиве')
    #events = models.ManyToManyField(Event, blank=True, related_name='blogs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name