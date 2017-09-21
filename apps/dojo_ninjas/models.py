from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return '%s %s %s %s' % (self.name, self.city, self.state, self.desc)
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas')
    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.dojo)