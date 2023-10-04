from django.contrib import admin
from  .models import *

# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','paramater','created_date','update_date']
    search_fields = ['name','paramater']
    list_editable = ['paramater']

    class Meta:
        model = GeneralSetting
