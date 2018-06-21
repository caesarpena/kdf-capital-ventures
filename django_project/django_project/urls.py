"""speedylends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from static_sitemaps.urls import *
from loans.views import *

sitemaps = {
	'static' : StaticSiteMap
	}


urlpatterns = [

        url(r'^$', HomeView.as_view(), name='index'),
	url(r'^Home/', HomeView.as_view(), name='index'),
	url(r'^Contact/', ContactView.as_view(), name='Contact'),
	url(r'^Loans/', LoanForm.as_view(), name='Loans'),
	url(r'^comp/', CompletedView.as_view(), name='Complete'),
    	url(r'^Business/', MortgageWizard.as_view([Business_Loans_Step1, Business_Loans_Step2,Business_Loans_Step3, Business_Loans_Step4,Business_Loans_Step5]), name='Business'),
    	url(r'^Mortgage/', MortgageWizard.as_view([MortgageFormStep1,MortgageFormStep2,MortgageFormStep3,MortgageFormStep4,MortgageFormStep5]), name='Mortgage'),
    	url(r'^Personal/', MortgageWizard.as_view([personal_Loans_Step1, personal_Loans_Step2]), name='Personal'),
   # url("^soc/", include("social_django.urls", namespace="social")),
    	url(r'^admin/', admin.site.urls),
    	#url(r'^sitemap.xml', include('static_sitemaps.urls')),
        url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]



