# Generated by Django 2.1.7 on 2019-05-15 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190502_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
