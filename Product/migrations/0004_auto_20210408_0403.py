# Generated by Django 3.1.7 on 2021-04-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_auto_20210408_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='fname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='invoice',
            name='lname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
