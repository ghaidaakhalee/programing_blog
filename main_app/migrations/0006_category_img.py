# Generated by Django 3.1.6 on 2021-02-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]