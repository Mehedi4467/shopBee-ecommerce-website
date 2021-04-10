# Generated by Django 3.1.7 on 2021-04-07 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0002_auto_20210407_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='product/'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_created=True)),
                ('shop', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('img', models.ImageField(blank=True, upload_to='product/')),
                ('price', models.CharField(max_length=200)),
                ('band', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('division', models.CharField(max_length=300)),
                ('phone', models.EmailField(max_length=300)),
                ('send_number', models.CharField(max_length=15)),
                ('txid', models.CharField(max_length=300)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]