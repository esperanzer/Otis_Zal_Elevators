from django.contrib import admin

from .models import Expenses
from .models import Repairs
from .models import Installations

class ExpensesAdmin(admin.ModelAdmin):

	list_display = ['expense_name', 'charges', 'customer', 'timestamp']

admin.site.register(Expenses, ExpensesAdmin)

class RepairsAdmin(admin.ModelAdmin):

	list_display = ['repair_name', 'cost', 'company', 'timestamp']

admin.site.register(Repairs, RepairsAdmin)

class InstallationsAdmin(admin.ModelAdmin):

	list_display = ['installation_name', 'company', 'cost', 'timestamp']

admin.site.register(Installations, InstallationsAdmin)

# Register your models here.

 



