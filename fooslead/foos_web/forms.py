from django import forms

class TeamForm(forms.Form):
    member_a = forms.CharField(max_length=200)
    member_b = forms.CharField(max_length=200)
    team = forms.CharField(max_length=200)
