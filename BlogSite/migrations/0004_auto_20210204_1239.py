# Generated by Django 3.1.5 on 2021-02-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSite', '0003_auto_20210204_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]