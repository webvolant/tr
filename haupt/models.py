# ~*~ coding: utf-8 ~*~
from django.db import models

class Post(models.Model):
	name = models.CharField('Title - Заголовок',max_length=240)
	def __unicode__(self):
         return self.name; 