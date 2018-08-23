from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.
class Expenses(models.Model):
    expense_name = models.CharField(max_length=255, null=True, blank=True, default=None)
    charges = models.CharField(max_length=200)
    customer = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
    	return self.expense_name

    def get_absolute_url(self):
        return reverse('projects:expenses_detail', kwargs={'pk': self.pk})


class Repairs(models.Model):
	
	repair_name = models.CharField(max_length=100, null=False, blank=False)
	company = models.CharField(max_length = 255)
	timestamp = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(unique=True, null=True, blank=True)
	cost = models.CharField(max_length = 55, default='none')

	expenses = models.ForeignKey(Expenses)

	def __unicode__(self):
		return self.repair_name

	def get_absolute_url(self):
		return reverse('projects:repair_detail', kwargs={'pk': self.pk})



class Installations(models.Model):
	installation_name = models.CharField(max_length=100, null=False, blank=False)
	company = models.CharField(max_length = 55)
	timestamp = models.DateTimeField(default=timezone.now)
	cost = models.CharField(max_length = 55, default='none')

	expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE)
	repairs = models.ForeignKey(Repairs, on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.installation_name

	def get_absolute_url(self):
		return reverse('projects:installation_detail', kwargs={'pk': self.pk})	

