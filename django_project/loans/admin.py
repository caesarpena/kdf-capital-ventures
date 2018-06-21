from django.contrib import admin

from .models import *

admin.site.register(Loans_Form_Business)
admin.site.register(Loans_Form_Mortgage)
admin.site.register(Loans_Form_Personal)

