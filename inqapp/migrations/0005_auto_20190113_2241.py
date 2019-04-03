# Generated by Django 2.1.5 on 2019-01-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inqapp', '0004_auto_20190113_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, help_text='Please upload an image', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='message',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
