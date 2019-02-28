from django import forms
class NameForm(forms.Form):
     search =forms.CharField(label='Player Name',max_length=50)
