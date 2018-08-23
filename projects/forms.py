from django import forms
from django.contrib.auth.models import User
from .models import Expenses, Repairs, Installations




class ExpensesForm(forms.ModelForm):

	class Meta:
		model = Expenses
		fields = ['expense_name', 'charges', 'customer', 'timestamp']



class RepairsForm(forms.ModelForm):

	class Meta:
		model = Repairs
		fields = ['repair_name', 'company', 'timestamp', 'cost']


class InstallationsForm(forms.ModelForm):
	class Meta:
		model = Installations
		fields = ['installation_name', 'company', 'timestamp', 'cost']


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email']


