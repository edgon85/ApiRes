from django.db import models

# Create your models here.

class CourseApp(models.Model):
	name = models.CharField(max_length=60, blank=False)
	author = models.CharField(max_length=35, blank=False)
	description = models.TextField()
	rating = models.FloatField(default=3)
	students = models.IntegerField(default=0)
	price = models.FloatField(default=0.0)
	photo = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')


	def __str__(self):
		return '%s' %self.name

