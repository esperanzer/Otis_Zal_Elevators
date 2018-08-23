from django.conf.urls import url
from django.conf.urls.static import static
from .models import Expenses
from .models import Repairs
from .models import Installations
from .views import Expenses 
from .views import Repairs
from .views import Installations

from . import views
app_name = 'projects'

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^expense/', views.ExpenseListView.as_view(), name='expense'),
  url(r'^repair/', views.RepairListView.as_view(), name='repair'),
  url(r'^installation/', views.InstallationListView.as_view(), name='installation'),
  url(r'^registration/$', views.UserFormView.as_view(), name='registration'),
  # url(r'^logout_user/$', views.logout_user, name='logout_user'),
  url(r'^expense_detail/(?P<pk>\d+)/detail/', views.ExpensesDetailView.as_view(), name = 'expenses_detail'),
  url(r'^expense-add/$', views. ExpensesCreate.as_view(), name = 'expense-add'),
  # son** do i need an expense-add.html peg for above? NO
  url(r'^repair_detail/(?P<pk>\d+)/detail', views.RepairsDetailView.as_view(), name = 'repair_detail'),
  url(r'^repair-add/$', views. RepairsCreate.as_view(), name = 'repair-add'),
  # son** do i need an Repairs-add.html peg for above?NO
  url(r'^installation_detail/(?P<pk>\d+)/detail', views.InstallationsDetailView.as_view(), name = 'installation_detail'),
  url(r'^installation-add/$', views. InstallationsCreate.as_view(), name = 'installation-add'),
  	
   	
]
