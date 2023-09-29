from django.contrib import admin
from Testapp.models import StudentInfo
# Register your models here.
class StInfo(admin.ModelAdmin):
    listInfo=['name','age','address']
admin.site.register(StudentInfo,StInfo)
