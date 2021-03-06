#Import stuf from DJango; stuff to build other stuff

from django import forms
from .models import Student




class StudentForm (forms.ModelForm):
    class Meta:
        model = Student
        #what should be editable/ visible
        #fields = ['full_name', 'email', 'age']

        #what is not to be seen
        exclude = ['last_updated']

        model = Student

    #to ensure our data ia validated even before it reaches the model
    def clean_age(self):
        age = self.cleaned_data.get('age')
        #set your conditions in here
        if age > 120:
            raise forms.ValidationError("You may be to old for this class")
        elif age < 10:
            raise forms.ValidationError("You may be to young")
        return age

class FeedbackForm(forms.Form): #imports from forms, not from any classes
    full_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message == 'Dirty':
            message = 'Clean'
        print(message)
        return message