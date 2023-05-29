from django.contrib import admin

# Register your models here.
from users.models import *
admin.site.register(Student,)
admin.site.register(Orders,)
admin.site.register(StudentsAddress,)