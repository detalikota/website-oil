# Generated by Django 3.2 on 2021-05-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210518_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='url',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
