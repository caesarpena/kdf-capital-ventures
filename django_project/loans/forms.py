from django import forms
from django.contrib.admin.widgets import * 
from django.forms import ModelForm
from django.forms.models import *
from loans.models import *
import datetime

#select loan form form
class LoanTypeForm(forms.ModelForm):
	class Meta: 
		model = Loans_Form_Business
		fields = ['typesofloan']
		labels ={
			'typesofloan': 'Type of Loan'
			}	

 
#mortgage form step1
class MortgageFormStep1(forms.ModelForm):
	class Meta:			
		model = Loans_Form_Mortgage
		fields = ['Mortgage_Loan_type','Mortgage_Loan_Purpose', 'HIWBU', 'm_property_type',]

		labels ={
			'Mortgage_Loan_type': 'Loan Type',
			'Mortgage_Loan_Purpose':'Loan Purpose',
			'HIWBU':'How will this property be used',
			'm_property_type':'Property Type',}		
#mortgage loans step2
class MortgageFormStep2(forms.ModelForm):
	class Meta:			
		model = Loans_Form_Mortgage
		fields = ['Payment_Term','Number_Units', 'Loan_Amount', 'Amortization_Type',
		'Down_Payment_Source',]

		labels ={
			'Number_Units': 'Number of Units',
			'Loan_Amount':'Est. Loan Amt ($)',
			}
#mortgage loans step3
class MortgageFormStep3(forms.ModelForm):
	class Meta:			
		model = Loans_Form_Mortgage
		fields = ['property_zipcode','property_value', 'second_morgage_q',]

		labels ={
			'second_morgage_q':'Do you have a second mortgage?',
			'property_zipcode':'Zip code of the property',
			'property_value':"Estimation of the property"+"'s"+" value $",
			}
#mortgage loans step5
class MortgageFormStep5(forms.ModelForm):
	class Meta:			
		model = Loans_Form_Mortgage
		fields = ['Full_Name','Address', 'Zip_Code', 'Date_Of_Birth',
	        'Contact_Number', 'Current_House', 'Email']

		labels ={
			'Current_House': '(Own/Rent)',
			}

		widgets = {
		'Date_Of_Birth': forms.SelectDateWidget(years=range(datetime.date.today().year-99, datetime.date.today().year-20)),
		}

#mortgage loans step4
class MortgageFormStep4(forms.ModelForm):
	class Meta:			
		model = Loans_Form_Mortgage
		fields = ['Years_of_Schooling','Marrital_Status', 'Employment_Status', 'Credit_Score',]


#personal loans form
class Personal_Loans_Form(forms.ModelForm):

	class Meta:
		model = Loans_Form_Personal
		fields = ['Personal_Loan_Purpose', 'Employment_Status', 'Credit_Score', 'Credit_Score', 'personal_cash_borrow',
		'Annual_Tax_Income']
		labels ={
			'Personal_Loan_Purpose': 'Loan Purpose',
		 	'personal_cash_borrow': 'How much are you looking to borrow',
			}

  #Business Loans Form Step1
class Business_Loans_Step1(forms.ModelForm):

	class Meta:
		model = Loans_Form_Business
		fields = ['Business_Type','Amount_Requested','Minimum_Amount', 'Reason']

		labels ={
			'Amount_Requested': 'Amount Requested $','Minimum_Amount': 'Minimum Amount Needed $',
			'Reason': 'Describe the Type of Loan, Reason for your Loan and Use of Funds Requested - (Be specific)', 			
			}

  #Business Loans Form Step 2
class Business_Loans_Step2(forms.ModelForm):

	class Meta:
		model = Loans_Form_Business
		fields = ['Business_Name','DBA', 'State_Tax_ID_Number','Federal_Tax_ID_Number','Website','Business_Contact',
		'Business_Address', 'Business_City', 'Business_State', 'Business_Zipcode', 'Owner_Full_Name',]

		labels ={
			'Business_Name': 'Legal Business Name','Business_Contact': 'Business Contact #','Business_City': 'City',
			'Business_State': 'State', 'Business_Zipcode': 'Zipcode',}


  #Business Loans Form Step 3
class Business_Loans_Step3(forms.ModelForm):

	class Meta:
		model = Loans_Form_Business
		fields = ['Total_Assets','Net_Worth', 'Nature_of_Business',
		'Business_Inception_Date', 'Annual_Revenue',]

		labels ={
			'Total_Assets': 'Total Assets $','Net_Worth': 'Net Worth $','Nature_of_Business': 'Nature of the Business',
			}
		widgets = {
		'Business_Inception_Date': forms.SelectDateWidget(years=range(datetime.date.today().year-120, datetime.date.today().year+1)),
		}
  #Business Loans Form Step 4
class Business_Loans_Step4(forms.ModelForm):

	class Meta:
		model = Loans_Form_Business
		fields = ['bankruptcy_q','profit_q','Business_Zipcode',]

		labels ={
			'bankruptcy_q': 'Have your business filed in bankrunpcy in the last 2 years?', 
			'profit_q': 'Is the business been profitable in last 3 years?',
			}
  #Business Loans Form Step 5
class Business_Loans_Step5(forms.ModelForm):

	class Meta:
		model = Loans_Form_Business
		fields = ['Full_Name','Address', 'Zip_Code','Date_Of_Birth',
		'Email', 'Credit_Score']

		widgets = {
		'Date_Of_Birth': forms.SelectDateWidget(years=range(datetime.date.today().year-99, datetime.date.today().year-20)),
		}


#perosnal loan form
class personal_Loans_Step1(forms.ModelForm):

	class Meta:
		model = Loans_Form_Personal
		fields = ['Personal_Loan_Purpose','personal_cash_borrow', 'Credit_Score', 'Employment_Status',
		'Annual_Tax_Income', 'Current_House', 'Years_of_Schooling',]
		labels ={
			'Personal_Loan_Purpose': 'Loan Purpose', 
			'personal_cash_borrow': 'How much are you looking to borrow ($)',
			}

class personal_Loans_Step2(forms.ModelForm):

	class Meta:
		model = Loans_Form_Personal
		fields = ['Full_Name','Address', 'Zip_Code', 'Date_Of_Birth',
		'Contact','Email']
		labels ={
			'Contact': 'Contact Number', 
			}
		widgets = {
		'Date_Of_Birth': forms.SelectDateWidget(years=range(datetime.date.today().year-99, datetime.date.today().year-20)),
		}




# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)

# class ContactForm2(forms.Form):
#     sender = forms.CharField(widget=forms.Textarea)


# class ContactForm3(forms.Form):
#     message = forms.CharField(widget=forms.Textarea)
#     
