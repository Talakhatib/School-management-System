# Generated by Django 4.1 on 2022-08-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='language',
            field=models.CharField(choices=[('en', 'english'), ('fr', 'french')], max_length=10),
        ),
    ]
