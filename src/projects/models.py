from django.db import models


class Project(models.Model):
	"""added a class to hold the summary of the projects"""  # noqa: E117, W191
	title = models.CharField(max_length=120)  # noqa: W19
	description = models.TextField()
	project_url = models.CharField(max_length=120)  # noqa: W191
	git = models.CharField(max_length=120)  # noqa: W191
	status = models.CharField(max_length=120, default="Under Development")
