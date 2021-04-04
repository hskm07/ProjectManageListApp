from django import forms
from .models import Department, ProjectTeam

class SearchForm(forms.Form):
    department = forms.ModelChoiceField(
        queryset=Department.objects, label='Department', required=False
    )

    projectname = forms.ModelChoiceField(
        queryset=ProjectTeam.objects, label='ProjectTeam', required=False
    )