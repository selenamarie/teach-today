from django.db import models

# Create your models here.

class Lesson(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()

	def __unicode__(self):
		return self.name

class Promise(models.Model):
	who = models.CharField(max_length=200)
	when = models.DateTimeField('when')
	lesson = models.ForeignKey(Lesson)
	done = models.BooleanField(default=False)

	def __unicode__(self):
		return self.who + self.when + self.lesson.name
