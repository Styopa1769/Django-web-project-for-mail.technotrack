# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Place(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='places',
        verbose_name=u'Автор'
    )
    name = models.CharField(max_length=255, verbose_name=u'Имя места')
    is_archive = models.BooleanField(default=False, verbose_name=u'Место в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, verbose_name=u'Координаты места')

    class Meta:
        verbose_name = u'Место'
        verbose_name_plural = u'Места'
        ordering = 'name', 'id'


    def __unicode__(self):
        return self.name
