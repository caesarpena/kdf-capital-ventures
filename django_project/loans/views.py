from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext  # For CSRF
from django.shortcuts import render
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
#import arrow
from django.conf import settings
from django.forms import inlineformset_factory
from formtools.wizard.views import SessionWizardView
from django.contrib import messages
from django.core.mail import send_mail
from django.views import View
from .models import *
from .forms import *



class HomeView(View):
	def get(self, request):		
		return render(request, "index.html", {})

class ContactView(View):
	def get(self, request):	
		return render(request, "contact.html", {})		

class CompletedView(View):
	def get(self, request):
		return render(request, "completed.html", {})


class LoanForm(View):
	def get(self, request, *args, **kwargs):
		loan_type_form = LoanTypeForm()
		context = {
			"form": loan_type_form,
			}
		return render(request, "Form_View.html", context)

	def post(self, request, *args, **kwargs):

		loan_type = request.POST.get('typesofloan')

		if loan_type !=  None:
			return HttpResponseRedirect('/'+loan_type+'/')
                       # send_mail('New Loan Request', 'jhgf', ['info@kdfcapitalventures.com'], ['cesar_raynell@hotmail.com'], fail_silently=True)

class MortgageWizard(SessionWizardView):


	def done(self, form_list, **kwargs):		
		form_data = process_form_data(form_list)
		# context = {
		# 	"form_data": form_data,
		# 	}
		# return render("index2.html", context)
		return HttpResponseRedirect('/comp/')


def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	clean_data = form.cleaned_data
	reciepment_email = clean_data['Email']
	ClientEmailBody = 'Thank you for submiting your request, we will reach to you as soon as posible.'
	
	data_to_db(form_data)

	send_mail('New Loan Request', str(form_data), ['cesar.raynell@gmail.com'], ['info@kdfcapitalventures.com'], fail_silently=True)
	#send_mail('Loan Request', ClientEmailBody, ['info@kdfcapitalventures.com'], [reciepment_email], fail_silently=True)

	# print (form_data[0]['subject'])
	# print (form_data[1]['sender'])
	# print (form_data[2]['message'])
	


def data_to_db(form_list):
	data = {}
# being list_form a iterable list of forms
	for form in form_list:
		data.update(form)
	try:
		Loans_Form_Business.objects.create(**data)
	except Exception, e:
		print e
	try:
		Loans_Form_Mortgage.objects.create(**data)
	except Exception, e:
		print e
	try:
                Loans_Form_Personal.objects.create(**data)
        except Exception, e:
                print e



class StaticSiteMap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
	return ['index','Contact']

    def location(self,item):
        return reverse(item)
#arrow.now().format('YYYY-MM-DD')
