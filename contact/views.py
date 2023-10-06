from django.shortcuts import render
from django.http import JsonResponse
from core.models import Document,ImageSetting
from contact.models import Message
from contact.forms import contactForm
# Create your views here.
def contact_form(request):
    if request.POST:
        contact_form = contactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            success = True
            message = 'Contact form sent succesfully'
        else:
            success=False
            message='Contact form is not avalid'



    else:
        success = False
        message = 'Request method is not valid'

    context = {
        'success': success,
        'massage': message,
    }
    return JsonResponse(context)
def contact(request):
    contact_form=contactForm()
    context={
        'contact_form':contact_form
    }

    return render(request,'contact.html',context)
