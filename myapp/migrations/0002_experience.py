# Generated by Django 4.1.7 on 2023-03-31 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
