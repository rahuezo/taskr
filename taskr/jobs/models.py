# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} {1}".format(self.pk, self.title)
