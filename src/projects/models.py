from django.db import models

# Create your models here.
class Project(models.Model):
	"""added a class to hold the summary of the projects"""
	title = models.CharField(max_length=120)
	description = models.TextField()
	project_url = models.CharField(max_length=120)
	git = models.CharField(max_length=120)
	status = models.CharField(max_length=120, default="Under Development")