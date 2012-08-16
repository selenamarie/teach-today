from django import forms #cuz it is a package

# lolling about the difference between ModelForm and Form
class LessonAddForm(forms.Form):
	name = forms.CharField()
	url = forms.URLField() # IT BETTER VALIDATE IT

class PromiseForm(forms.Form):
	done = forms.BooleanField()
