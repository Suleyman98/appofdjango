from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

def upload_location(instance, filename):
	file_path = 'posts/{title}-{filename}'.format(
				 title=str(instance.title), filename=filename)
	return file_path


class BlogPost(models.Model):
	title 					= models.CharField(max_length=50, null=False, blank=False)
	body 					= models.TextField(max_length=60, null=False, blank=False)
	image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
	slug 					= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title
class TechPost(models.Model):
	title 					= models.CharField(max_length=50, null=False, blank=False)
	body 					= models.TextField(max_length=60, null=False, blank=False)
	image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
	slug 					= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.title
 