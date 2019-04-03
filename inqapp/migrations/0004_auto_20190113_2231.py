# Generated by Django 2.1.5 on 2019-01-13 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inqapp', '0003_auto_20190113_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default='temp', help_text='Please upload an image', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='message',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]