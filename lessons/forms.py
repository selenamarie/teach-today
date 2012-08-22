from django import forms #cuz it is a package
import datetime

from lessons.models import Lesson, Assessment

# lolling about the difference between ModelForm and Form
class LessonAddForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField() # IT BETTER VALIDATE IT

choices = ( (1,'Yes'),
            (0,'Not yet'),
          )

# I HATE CHOICE FIELDS
class PromiseForm(forms.Form):
    done = forms.TypedChoiceField(choices=choices, widget=forms.RadioSelect, coerce=int, label="I did it!")

# I HATE CHOICE FIELDS
class PromiseMakeForm(forms.Form):
    who = forms.CharField()
    when = forms.DateField(initial=datetime.date.today)
    made_by = forms.IntegerField()
    #lesson = forms.ChoiceField()
# http://stackoverflow.com/questions/3419997/creating-a-dynamic-choice-field
    def __init__(self, *args, **kwargs):
        super(PromiseMakeForm, self).__init__(*args, **kwargs)
        self.fields['lesson'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Lesson.objects.all()])
        self.fields['assessment'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Assessment.objects.all()])

class AssessmentForm(forms.Form):
    post = forms.CharField()

class AssessmentAddForm(forms.Form):
    question = forms.CharField(max_length=200)
