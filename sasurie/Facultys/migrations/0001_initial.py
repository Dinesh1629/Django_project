# Generated by Django 4.2.3 on 2023-08-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField()),
                ('F_id', models.IntegerField()),
                ('Department', models.CharField()),
                ('Designation', models.CharField()),
                ('Qualification', models.CharField()),
                ('Experience', models.PositiveIntegerField()),
                ('Contact', models.PositiveIntegerField(max_length=10)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
    ]
