from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').paramater
    site_keywords=GeneralSetting.objects.get(name='site_keywords').paramater
    site_description=GeneralSetting.objects.get(name='site_description').paramater

    home_banner_name=GeneralSetting.objects.get(name='home_banner_name').paramater
    home_banner_title=GeneralSetting.objects.get(name='home_banner_title').paramater
    home_banner_description=GeneralSetting.objects.get(name='home_banner_description').paramater

    about_myself=GeneralSetting.objects.get(name='about_myself').paramater
    about_footer = GeneralSetting.objects.get(name='about_footer').paramater
    
    home_banner_image=ImageSetting.objects.get(name='home_banner_image').file
    header_image = ImageSetting.objects.get(name='header_image').file
    favicon = ImageSetting.objects.get(name='favicon').file
    skills=Skill.objects.all().order_by('order')
    context={
        'site_title':site_title,
        'site_keywords':site_keywords,
        'site_description':site_description,
        'home_banner_name':home_banner_name,
        'home_banner_title':home_banner_title,
        'home_banner_description':home_banner_description,
        'about_myself':about_myself,
        'about_footer':about_footer,
        'home_banner_image': home_banner_image,
        'header_image':header_image,
        'favicon':favicon,
        'skills':skills,

    }
    return render(request,'index.html',context)

