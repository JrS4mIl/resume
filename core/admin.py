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

@admin.register(Experince)
class ExperinceAdmin(admin.ModelAdmin):
    list_display = ['id','company_name','job_title','job_location','start_date','end_date','created_date','update_date']
    search_fields = ['name','company_name']
    list_editable = ['company_name','job_title','job_location','start_date','end_date']


    class Meta:
        model=Experince
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id','school_name','major','departman','start_date','end_date','created_date','update_date']
    search_fields = ['name','school_name']
    list_editable = ['school_name','major','departman','start_date','end_date']


    class Meta:
        model=Education

@admin.register(SosyalMedia)
class SosyalMediaAdmin(admin.ModelAdmin):
    list_display = ['id','link','icon','created_date','update_date']
    search_fields = ['link']
    list_editable = ['link','icon']



    class Meta:
        model=SosyalMedia

