# Generated by Django 2.1.7 on 2019-05-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_mix_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='mix',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
