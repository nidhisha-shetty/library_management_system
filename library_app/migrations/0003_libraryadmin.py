# Generated by Django 4.0.4 on 2022-05-17 01:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0002_lib_delete_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libraryadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinValueValidator(7000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('age', models.IntegerField(max_length=100)),
                ('dob', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]