from django.db import models
from django.core.validators import RegexValidator


#CurDate = 

Credit_Score_Choices = (
    ('excellent', 'Excellent ( => 720)'), ('good', 'Good (680 - 719)'),('fair', 'Fair (640 - 679)'),
    ('poor', 'Poor ( =<639)'),
    )

BoolChoice = (
    (0, 'No'),
    (1, 'Yes'),
    )
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="# must be entered in the format: '+999999999'. Up to 15 digits allowed.")
zipcode_regex = RegexValidator(regex=r'^\+?1?\d{0,5}$', message="Zip code must be entered in the format: '99999'. Up to 5 digits allowed.")

Employment_Status_Choice=[
    ('full_time','Full Time'),('part_time','Part Time'),('self_employed','Self Employed'),
    ('unemployed','Unemployed'),('other','Other'),
    ]

schooling_choices = [
    ('8thgrd','8th Grade'), ('9thgrd', '9th Grade'),('10thgrd','10th Grade'),('11thgrd','11th Grade'),('Hight_School_Graduate','Hight School Graduate'),
    ('1_Yr_College','1 Year College'),('assotiates_degree','Associates Degree'),('3_Yr_College','3 Year College'),
    ('bachelors','Bachelors Degree'),('jd','JD'),('md','MD'),('phd','PhD'),]

# commercial_loan_Choices=[
#     ('Acquisition_and_development','Acquisition and development'),('Bond','Bond'),('Bridge_loans','Bridge loans'),
#     ('Construction','Construction'),('Forward_commitments','Forward commitments'),('Joint_ventures','Joint ventures'),
#     ('Mezzanine','Mezzanine'),('Nonrecourse','Nonrecourse'),('Notes_purchased','Notes purchased'),('Purchase','Purchase'),
#     ('Refinance_Cash-Out','Refinance: Cash-Out'),('Refinance_Rate-and-Term','Refinance: Rate and Term'),
#     ('Remodel/renovation','Remodel/renovation'),('SBA loans','SBA loans'),('Second_mortgages ','Second mortgages '),
#     ]

# commercial_loan_Choices=[
#     ('Acquisition','Acquisition of property'),('development','Development'),('Refinance','Refinance'),
#     ('Business_Expansion','Business Expansion'),('Raw_Land_Purchase','Raw Land Purchase'),]
# Fixed_Rate_Choice=[
#     ('1_Year','1 Year Fixed'),('2_Year','3 Years Fixed'),('5_Years','5 Years Fixed'),('7_Years','7 Years Fixed'),
#     ('10_Years','10 Years Fixed'),('10-20_Years','10-20 Years Fixed'),('20-30_Years','20-30 Years Fixed'),]
# Amortization_Choice=[
#     ('5_Year','5 Years'),('10_Year','10 Years'),('15_Years','15 Years'),('20_Years','20 Years'),
#     ('25_Years','25 Years'),('30_Years','30 Years'),]
# When_Loan_Choice=[
#     ('RightNow','Right Now'),('1-2weeks','1-2 Weeks'),('4weeks','Withing 4 weeks'),('6weeks','Withing 6 weeks'),
#     ('2month','Withing 2 month'),('3month','Withing 3 month'),('4month','Withing 4 month'),('5month','Withing 5 month'),
#     ('6month','Withing 6 month'),('+6month','More than 6 month'),


# commercial_property_type_Choice=[
#     ('Agricultural','Agricultural (ranches and farms)'),('Automotive','Automotive (gas stations, carwashes, etc.)'),('Churches','Churches'),
#     ('Industrial','Industrial'),('Leisure','Leisure (golf courses, marinas, RV parks, etc.)'),('Medical','Medical (hospitals, clinics, etc.)'),
#     ('Mixed-use_properties','Mixed-use properties'),('Mobile/manufactured','Mobile/manufactured home parks'),('Office_buildings/complexes','Office buildings/complexes'),
#     ('Office_condos','Office condos'),('Parking_lot_sites','Parking lot sites'),('Rehabilitation_facilities','Rehabilitation facilities'),('Retail_(shopping)','Retail (shopping centers/strip malls)'),
#     ('Self-storage','Self-storage'),('Single-tenant_buildings','Single-tenant buildings'),
#     ]




class Loans_Form_Business(models.Model):

    Business_Type_Choices=[
    ('sole_propietorship','Sole Propietorship'),('partnership','Partnership'),('corporation','Corporation'),
    ('s_Corporation','S Corporation'),('limited_liability_company','Limited Liability Company (LLC)'),
    ]
    
    LOAN_CHOICES = [
         ('Personal','PERSONAL LOAN'),
        ('Business', 'BUSINESS LOAN'),('Mortgage','MORTGAGE LOAN')
        ]

    typesofloan = models.CharField(max_length=50,choices=LOAN_CHOICES, default='personal')
        #Business Loan fields
    Business_Type = models.CharField(max_length=50,choices=Business_Type_Choices, default='')
    Amount_Requested = models.DecimalField(max_digits=20,decimal_places=2)
    Minimum_Amount = models.DecimalField(max_digits=20,decimal_places=2)
    Reason = models.TextField(max_length=1000,default='')

    Business_Name = models.CharField(max_length=50)
    DBA = models.CharField(max_length=50, blank=True)
    State_Tax_ID_Number = models.IntegerField(blank=True)
    Federal_Tax_ID_Number = models.IntegerField(blank=True)
    Business_Contact = models.CharField(max_length=15,validators=[phone_regex])
    Business_Address = models.CharField(max_length=50)
    Business_City = models.CharField(max_length=50)
    Business_State = models.CharField(max_length=50)
    Business_Zipcode = models.CharField(max_length=5,validators=[zipcode_regex])
    Owner_Full_Name = models.CharField(max_length=50)

    Total_Assets = models.DecimalField(max_digits=20,decimal_places=2)
    Net_Worth = models.DecimalField(max_digits=20,decimal_places=2)
    Nature_of_Business = models.CharField(max_length=50)
    Website = models.URLField(blank=True)
    Business_Inception_Date = models.DateField()  
    Annual_Revenue = models.CharField(max_length=50)

    bankruptcy_q = models.IntegerField(choices=BoolChoice, default=0, null=True)
    profit_q = models.IntegerField(choices=BoolChoice, default=0, null=True)    
#personal fields
    Full_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Zip_Code = models.CharField(max_length=5,validators=[zipcode_regex])
    Date_Of_Birth = models.DateField()
    Email = models.EmailField(max_length=50)
    Credit_Score = models.CharField(max_length=50,choices=Credit_Score_Choices, default='')


class Loans_Form_Mortgage(models.Model): 

    payment_term_choice=[
    ('50_Year','50 Years'),('40_Year','40 Years'),('30_Years','30 Years'),('20_Years','20 Years'),
    ('15_Years','15 Years'),('10_Years','10 Years'),('7_Years','7 Years'),('5_Years','5 Years'),]
    Mortgage_loan_type_Choices = [
    ('conventional','Conventional'), ('va', 'VA'),('fha','FHA'),
    ('usda_ruralhousing','USDA/Rural Housing'),('hard_money','Hard Money'),
    ('other','Other'),]
    number_units_choices = [
    ('0','0'), ('1', '1'),('2','2'),('3','3'),('4','4'),]
    down_payment_choices = [
    ('sale','Sale Of Existing'), ('savings', 'Savings'),('equity','Equity'),('gift','Gift'),]
    amortization_type_choice = [
    ('fixed','Fixed Rate'), ('adjustable', 'Adjustable Rate'),('other','Other Loan Payment Type'),]
    Mortgage_loan_choices = [
    ('refinance','REFINANCE'), ('buyhome', 'BUY HOME'),('homeequity','HOME EQUITY LOAN'),
    ('reverse','REVERSE MORTGAGE LOAN'),]
    HIWBU_CHOICES=[
    ('primary','Primary Home'),('secondary','Secondary Home'),('rental','Rental Property') ]
    PT_CHOICES=[
    ('single_family_home','Single Family Home'),('Townhome','Townhome'),('condo','Condo'),
    ('multi_family_dwelling','Multi Family Dwelling'),('mobile_manufactured_home','Mobile/Manufactured Home')]

    #Step 1 
    Mortgage_Loan_type = models.CharField(max_length=50,choices=Mortgage_loan_type_Choices, default='')
    Mortgage_Loan_Purpose = models.CharField(max_length=50,choices=Mortgage_loan_choices, default='')
    HIWBU = models.CharField(max_length=50,choices=HIWBU_CHOICES, default='')
    m_property_type = models.CharField(max_length=50,choices=PT_CHOICES, default='')
        #Step 2
    Payment_Term = models.CharField(max_length=50,choices=payment_term_choice, default='')
    Number_Units = models.CharField(max_length=50,choices=number_units_choices, default='')
    Loan_Amount =  models.DecimalField(max_digits=20,decimal_places=2)
    Amortization_Type = models.CharField(max_length=50,choices=amortization_type_choice, default='')
    Down_Payment_Source = models.CharField(max_length=50,choices=down_payment_choices, default='')
        #Step 3
    property_zipcode = models.CharField(max_length=5,validators=[zipcode_regex])
    property_value =  models.DecimalField(max_digits=20,decimal_places=2)
    second_morgage_q = models.IntegerField(choices=BoolChoice, default=0, null=True)
        #Step 4 Personal
    Full_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Zip_Code = models.CharField(max_length=5,validators=[zipcode_regex])
    Date_Of_Birth = models.DateField()
    Contact_Number = models.CharField(max_length=15,validators=[phone_regex], blank=True)
    Current_House = models.CharField(max_length=50,choices=[('own','Own'),('rent','Rent'),], default='')
    Email = models.EmailField(max_length=50)
        # Step 5
    Years_of_Schooling = models.CharField(max_length=50,choices=schooling_choices, default='')
    Marrital_Status = models.CharField(max_length=50,choices=[('single','Single'),('married','Married'),], default='')
    Employment_Status = models.CharField(max_length=50,choices=Employment_Status_Choice, default='')
    Credit_Score = models.CharField(max_length=50,choices=Credit_Score_Choices, default='')


class Loans_Form_Personal(models.Model): 

    PL_CHOICES_1=[
    ('debt_consolidation','Debt Consolidation'),('credit_card_consolidation','Credit Card Consolidation'),
    ('home_improvement','Home Improvement'),('home_buying','Home Buying'),('majot_purchase','Major Purchase'),
    ('car_financing','Car Financing'),('green_loan','Green Loan'),('business','Business'),('vacation','Vacation'),
    ('wedding_expenses','Wedding Expenses'),('moving_relocation','Moving Relocation'),('other','Other')
    ]

    #Personal loan fields
    Personal_Loan_Purpose = models.CharField(max_length=50,choices=PL_CHOICES_1, default='')
    personal_cash_borrow = models.IntegerField()
    Credit_Score = models.CharField(max_length=50,choices=Credit_Score_Choices, default='')
    Employment_Status = models.CharField(max_length=50,choices=Employment_Status_Choice, default='')
    Annual_Tax_Income = models.IntegerField()
    Current_House = models.CharField(max_length=50,choices=[('own','Own'),('rent','Rent'),], default='')
    Years_of_Schooling = models.CharField(max_length=50,choices=schooling_choices, default='')

    #personal fields
    Full_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Zip_Code = models.CharField(max_length=50)
    Date_Of_Birth = models.CharField(max_length=50)
    Contact = models.CharField(max_length=15,validators=[phone_regex])
    Email = models.CharField(max_length=50)

    #Commercial Loan fields
    # Commercial_loantype= models.CharField(max_length=50,choices=commercial_loan_Choices, default='')
    # Requested_Rate = models.CharField(max_length=50,choices=Fixed_Rate_Choice, default='')
    # Request_Amortization = models.CharField(max_length=50,choices=Fixed_Rate_Choice, default='')
    # When_Need_theLoan = models.CharField(max_length=50,choices=When_Loan_Choice, default='')
    # c_property_type= models.CharField(max_length=50,choices=commercial_property_type_Choice, default='') #check

    # Business_Inception_Date = models.CharField(max_length=50)
    # Annual_Revenue = models.CharField(max_length=50)
    # bankruptcy_q = models.IntegerField(choices=BoolChoice, default=0, null=True)
    # profit_q = models.IntegerField(choices=BoolChoice, default=0, null=True)
    # Business_Name = models.CharField(max_length=50)
    # Business_Zipcode = models.CharField(max_length=5)
    # Credit_Score = models.CharField(max_length=50,choices=Credict_Score_Choices, default='')
    # Owner_Full_Name = models.CharField(max_length=50)


    


