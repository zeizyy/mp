from django.db import models

# Create your models here.
class Mentor(models.Model):
	name = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	gender = models.CharField(max_length=10)
	year = models.CharField(max_length=10)
	school = models.CharField(max_length=30)
	home = models.CharField(max_length=30)
	high = models.CharField(max_length=20)
	major = models.CharField(max_length=40)
	work = models.CharField(max_length=200)
	intro = models.CharField(max_length=2000)
	ec = models.CharField(max_length=2000)
	hobby = models.CharField(max_length=2000)
	three = models.CharField(max_length=40)
	clas = models.CharField(max_length=1000)
	music = models.CharField(max_length=1000)
	movie = models.CharField(max_length=1000)
	book = models.CharField(max_length=1000)
	quote = models.CharField(max_length=100)
	photo = models.CharField(max_length=300)

	def __str__(self):
		return self.name


