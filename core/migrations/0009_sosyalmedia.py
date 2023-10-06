# Generated by Django 4.2.5 on 2023-10-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='SosyalMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default='0', verbose_name='Order')),
                ('link', models.URLField(blank=True, default='', verbose_name='Link')),
                ('icon', models.CharField(blank=True, default='', max_length=200, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'SosyalMedia',
                'verbose_name_plural': 'SosyalMedias',
                'ordering': ('order',),
            },
        ),
    ]