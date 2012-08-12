from django.db import models

# Create your models here.

class Lesson(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()
	pub_date = models.DateTimeField('pub_date')

	def __unicode__(self):
		return self.name

class Promise(models.Model):
	who = models.CharField(max_length=200)
	when = models.DateTimeField('when')
	lesson = models.ForeignKey(Lesson)
	done = models.BooleanField(default=False)

	def __unicode__(self):
		return "Teach <a href='/lessons/%i/'>%s</a> for <strong>%s</strong> on " % (self.lesson.id, self.lesson.name, self.who)
