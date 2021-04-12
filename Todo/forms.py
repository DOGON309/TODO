from django import forms

class Loginform(forms.Form):
	username = forms.CharField(label = 'Username', max_length=100, widget = forms.TextInput(attrs = {'class':'form-control'}))
	password = forms.CharField(label = 'Password', max_length=1000, min_length = 8, widget = forms.PasswordInput(attrs={'class':'form-control'}))

class Indexform(forms.Form):
	SELECT = (('高', ' 高'), ('中', ' 中'), ('低', '低'))
	todo = forms.CharField(label = 'todo', max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
	choice = forms.ChoiceField(label = 'choice', choices = SELECT, widget = forms.Select(attrs={'class': 'form-control'}))