from django.shortcuts import render,redirect,get_object_or_404
from .models import *

# Create your views here.

def get_general_setting(parameter):
    try:
        obj=GeneralSetting.objects.all(name=parameter).parameter
    except:
        obj= ''
    return obj

def get_image_setting(parameter):
    try:
        obj=ImageSetting.objects.all(name=parameter).file
    except:
        obj= ''
    return obj


def layout(request):

    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    about_myself = get_general_setting('about_myself')
    about_footer = get_general_setting('about_footer')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')



    home_banner_image = get_image_setting('home_banner_image')
    header_image = get_image_setting('header_image')
    favicon = get_image_setting('favicon')
    sosyalmedias = SosyalMedia.objects.all()

    documents = get_general_setting('documents')
    context={
        'documents':documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself': about_myself,
        'about_footer': about_footer,
        'home_banner_image': home_banner_image,
        'header_image': header_image,
        'favicon': favicon,
        'sosyalmedias': sosyalmedias,
    }
    return context

def index(request):

    skills=Skill.objects.all().order_by('order')
    educations=Education.objects.all()

    experinces=Experince.objects.all()





    context={

        'skills':skills,
        'experinces':experinces,
        'educations':educations,



    }
    return render(request,'index.html',context)

def redirect_urls(request,slug):
    doc=get_object_or_404(Document,slug=slug)

    return redirect(doc.file.url)