# Generated by Django 3.0.6 on 2020-06-01 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilitators', '0002_auto_20200531_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='tprofile',
            field=models.FileField(upload_to='facilitators/profile'),
        ),
    ]