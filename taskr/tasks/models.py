# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from jobs.models import Job


class Task(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255, blank=True, default="", null=True)
    date = models.DateField(default=timezone.now)
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)
    notes = models.CharField(max_length=255, blank=True, default="", null=True)

    def save(self, *args, **kwargs):
        """On save, set task title"""
        if len(self.title) == 0:
            self.title = "Task {0}".format(timezone.now().strftime('%m%d%y'))
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
