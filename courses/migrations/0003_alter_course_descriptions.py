# Generated by Django 4.1 on 2022-08-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='descriptions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
