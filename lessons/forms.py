from django import forms #cuz it is a package


# lolling about the difference between ModelForm and Form
class LessonAddForm(forms.Form):
	name = forms.CharField()
	url = forms.URLField() # IT BETTER VALIDATE IT

choices = ( (1,'True'),
            (0,'False'),
          )

# I HATE CHOICE FIELDS
class PromiseForm(forms.Form):
	done = forms.TypedChoiceField(choices=choices, widget=forms.RadioSelect, coerce=int)
