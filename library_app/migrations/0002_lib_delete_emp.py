# Generated by Django 4.0.4 on 2022-05-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Emp',
        ),
    ]