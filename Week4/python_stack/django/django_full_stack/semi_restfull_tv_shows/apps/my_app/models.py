from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    if len(postData['title']) <= 2:
      errors['title'] = "You need to add more than 2 letters on tittle assHOL"
    if len(postData['network']) <= 3:
      errors['network'] = "put more than 3 characters in netwework"
    if len(postData['desc']) <= 10:
      errors['desc'] = "put more than 3 characters in descriptions assHOL"
    return errors



class Show(models.Model):
  title = models.CharField(max_length=50)
  network = models.CharField(max_length=50)
  release_date = models.DateTimeField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = ShowManager()
