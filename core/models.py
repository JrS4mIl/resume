from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class AbstractModel(models.Model):
    update_date = models.DateTimeField(blank=True, auto_now=True)
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        abstract=True
class GeneralSetting(AbstractModel):
    name=models.CharField(default='',max_length=100,blank=True)
    description=models.CharField(default='',max_length=254,blank=True)
    paramater=models.CharField(default='',max_length=254,blank=True)

    def __str__(self):
        return f'General Setting:{self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)

class ImageSetting(AbstractModel):
    name=models.CharField(default='',max_length=120,blank=True,verbose_name='Name')
    description = models.CharField(default='', max_length=254, blank=True)
    file=models.ImageField(default='',verbose_name='Image',blank=True,upload_to='images/')

    def __str__(self):
        return f'Image Setting:{self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)
class Skill(AbstractModel):
    order=models.IntegerField(default='0',verbose_name='Order')
    name=models.CharField(default='',max_length=120,blank=True,verbose_name='Name')
    percentage=models.IntegerField(default=50,verbose_name='Percentage',validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return f'Skill:{self.name}'

    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'
        ordering=('order',)


class Experince(AbstractModel):
    company_name=models.CharField(default='',max_length=120,blank=True,verbose_name='Company Name')
    job_title=models.CharField(default='',max_length=120,blank=True,verbose_name='Job Title')
    job_location=models.CharField(default='',max_length=120,blank=True,verbose_name='Jop Location')
    start_date=models.DateField()
    end_date=models.DateField(default='',blank=True,null=True,verbose_name='End Date')

    def __str__(self):
        return f'Experince:{self.company_name}'

    class Meta:
        verbose_name = 'Experince'
        verbose_name_plural = 'Experinces'
        ordering = ('start_date',)

