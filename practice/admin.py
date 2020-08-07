from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(Testcase)
admin.site.register(Output)