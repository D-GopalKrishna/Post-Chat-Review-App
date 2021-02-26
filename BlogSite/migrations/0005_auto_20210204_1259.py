# Generated by Django 3.1.5 on 2021-02-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSite', '0004_auto_20210204_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]