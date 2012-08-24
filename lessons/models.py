from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Assessment(models.Model):
    question = models.CharField(max_length=200)
    # probably include possible answers, later

    def __unicode__(self):
        return self.question

class Promise(models.Model):
    who = models.CharField(max_length=200)
    when = models.DateTimeField('when')
    lesson = models.ForeignKey(Lesson)
    done = models.BooleanField(default=False)
    made_by = models.ForeignKey(User)
    assessment = models.ForeignKey(Assessment)

    def __unicode__(self):
        return "Teach <a href='/lessons/%i/'>%s</a> for <strong>%s</strong> on " % (self.lesson.id, self.lesson.name, self.who)

class AssessmentResponse(models.Model):
    pre = models.TextField(default='')
    post = models.TextField()
    promise = models.ForeignKey(Promise)

