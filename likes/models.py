# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='likes',
        verbose_name=u'Автор'
    )
    liked = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'like'
        verbose_name_plural = u'likes'
        ordering = 'created', 'id'

    def __unicode__(self):
        return u'like от {} к {} № {}'.format(self.author.username, self.content_type, self.object_id)


