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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments_for_profiles',
        verbose_name=u'Автор'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='received_comments',
        verbose_name=u'Адресат'
    )
    is_archive = models.BooleanField(default=False, verbose_name=u'Комментарий в архиве')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000,verbose_name='Текст комментария')

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        ordering = 'created', 'id'
