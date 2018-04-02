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


class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments_for_events',
        verbose_name=u'Автор'
    )
    event = models.ForeignKey(
        Event,
        related_name='comments',
        verbose_name=u'Событие'
    )
    is_archive = models.BooleanField(default=False, verbose_name=u'Комментарий в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000,verbose_name='Текст комментария')

    class Meta:
        verbose_name = u'Комментарий к событию'
        verbose_name_plural = u'Комментарии к событиям'
        ordering = 'created', 'id'


class Tag(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tags_for_events',
        verbose_name=u'Автор'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    events = models.ManyToManyField(Event, blank=True, related_name='events')
    text = models.CharField(max_length=63, verbose_name='Текст тэга')

    class Meta:
        verbose_name = u'Тэг'
        verbose_name_plural = u'Тэги'
        ordering = 'created', 'id'
