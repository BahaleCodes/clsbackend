# Generated by Django 3.0.5 on 2020-11-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clsapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='field',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='fileName',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='fileType',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='table',
            field=models.CharField(max_length=32, null=True),
        ),
    ]