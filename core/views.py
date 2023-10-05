from django.shortcuts import render,redirect,get_object_or_404
from .models import *

# Create your views here.
def layout(request):
    documents = Document.objects.all()
    site_title = GeneralSetting.objects.get(name='site_title').paramater
    site_keywords = GeneralSetting.objects.get(name='site_keywords').paramater
    site_description = GeneralSetting.objects.get(name='site_description').paramater

    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').paramater
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').paramater
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').paramater

    about_myself = GeneralSetting.objects.get(name='about_myself').paramater
    about_footer = GeneralSetting.objects.get(name='about_footer').paramater

    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    header_image = ImageSetting.objects.get(name='header_image').file
    favicon = ImageSetting.objects.get(name='favicon').file
    sosyalmedias = SosyalMedia.objects.all()
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