from django.contrib import admin
from contact.models import Message
# Register your models here.
@admin.register(Message)
class MessagaAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','created_date','update_date']
    search_fields = ['name','subject']

    class Meta:
        model=Message