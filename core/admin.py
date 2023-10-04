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

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','created_date','update_date']
    search_fields = ['name','description','file']


    class Meta:
        model=ImageSetting

@admin.register(Skill)
class SkillSettingAdmin(admin.ModelAdmin):
    list_display = ['id','order','name','percentage','created_date','update_date']
    search_fields = ['name']
    list_editable = ['name','percentage','order']


    class Meta:
        model=Skill