# Generated by Django 4.2.5 on 2023-10-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_generalsetting_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=120, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254)),
                ('file', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image')),
            ],
        ),
    ]