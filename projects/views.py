from .models import Expenses
from .models import Repairs
from .models import Installations
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q
from django.contrib.auth import authenticate, login
from .forms import ExpensesForm, RepairsForm, InstallationsForm, UserForm




class IndexView(generic.ListView):
	template_name = 'projects/index.html'


	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		# context['expenses'] = Expenses.objects.all()
		return context

	def get_queryset(self):
		return 
	

	
class ExpenseListView(generic.ListView):
	template_name = 'projects/expense.html'
	model = Expenses
	# context_object_name = 'expenses'
	
	def get_context_data(self, **kwargs):
		context = super(ExpenseListView, self).get_context_data(**kwargs)
		context['expenses'] = Expenses.objects.all()
		return context

	def get_queryset(self):
		return Expenses.objects.all()

class RepairListView(generic.ListView):
	template_name = 'projects/repair.html'
	model = Repairs
	# context_object_name = 'repairs'
	
	def get_context_data(self, **kwargs):
		context = super(RepairListView, self).get_context_data(**kwargs)
		context['repairs'] = Repairs.objects.all()
		return context

	def get_queryset(self):
		return Repairs.objects.all()


class InstallationListView(generic.ListView):
	template_name = 'projects/installation.html'
	model = Installations
	# context_object_name = 'repairs'
	
	def get_context_data(self, **kwargs):
		context = super(InstallationListView, self).get_context_data(**kwargs)
		context['installations'] = Installations.objects.all()
		return context

	def get_queryset(self):
		return Installations.objects.all()

	# Expenses.objects.all()


class ExpensesDetailView(generic.DetailView):
	model = Expenses
	template_name = 'projects/expenses_detail.html'
	queryset = None

	def get_context_data(self, **kwargs):
		context = super(ExpensesDetailView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', None)
		context['expense'] = self.model.objects.get(pk=pk)
		return context



class RepairsDetailView(generic.DetailView):
	model = Repairs
	template_name = 'projects/repair_detail.html'
	# queryset = None

	def get_context_data(self, **kwargs):
		context = super(RepairsDetailView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', None)
		context['repair'] = self.model.objects.get(pk=pk)
		return context

class InstallationsDetailView(generic.DetailView):
	model = Installations
	template_name = 'projects/installation_detail.html'
	# queryset = None	

	def get_context_data(self, **kwargs):
		context = super(InstallationsDetailView, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', None)
		context['installation'] = self.model.objects.get(pk=pk)
		return context



class ExpensesCreate(CreateView):
	model = Expenses
	fields = ['expense_name', 'charges', 'customer', 'timestamp']
	success_url = ('/')

class RepairsCreate(CreateView):
	model = Repairs
	fields = ['repair_name', 'company', 'cost', 'timestamp']

class InstallationsCreate(CreateView):
	model = Installations
	fields = ['installation_name', 'company', 'cost', 'timestamp']

	# registaring user
class UserFormView(View):
	form_class = UserForm
	template_name = 'projects/registration_form.html'

		# display new form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# proces form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			# end user registration
			# retening User objects if credentios ar corect
			user = authenticate(username=username, password=password)
			if user is not none:
				if user.is_active:
					login(request, user)
					return redirect('projects:index')
		return render(request, self.template_name, {'form': form})




