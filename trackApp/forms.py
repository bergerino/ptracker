from django import forms
from datetime import date

class UserSpentOnProjectForm(forms.Form):
    name = forms.CharField(required=False, label='Jméno', max_length=100)
    project = forms.CharField(required=False, label='Projekt', max_length=100)
    year = forms.IntegerField( required=True, label='Rok', max_value=date.today().year)
    month = forms.IntegerField(required=True, min_value=1, max_value=12, label='Měsíc')

class UserSpentForm(forms.Form):
    name = forms.CharField(required=False, label='Jméno', max_length=100)
    year = forms.IntegerField( required=True, label='Rok', max_value=date.today().year)
    month = forms.IntegerField(required=True, min_value=1, max_value=12, label='Měsíc')

class ProjectSpentForm(forms.Form):
    name = forms.CharField(required=False, label='Projekt', max_length=100)
    year = forms.IntegerField( required=True, label='Rok', max_value=date.today().year)
    month = forms.IntegerField(required=True, min_value=1, max_value=12, label='Měsíc')