# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from events.models import Event


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


class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments_for_places',
        verbose_name=u'Автор'
    )
    place = models.ForeignKey(
        Place,
        related_name='comments',
        verbose_name=u'Место'
    )
    is_archive = models.BooleanField(default=False, verbose_name=u'Комментарий в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000,verbose_name='Текст комментария')
    class Meta:
        verbose_name = u'Комментарий к месту'
        verbose_name_plural = u'Комментарии к местам'
        ordering = 'created', 'id'
