# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, default='<i class="fa fa-calendar-plus-o" aria-hidden="true"></i>')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Activity {0} - {1}".format(self.pk, self.description)
