# Generated by Django 2.0 on 2019-04-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttabletitle',
            name='cl1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contenttabletitle',
            name='cl2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contenttabletitle',
            name='cl3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contenttabletitle',
            name='cl4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contenttabletitle',
            name='cl5',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contenttabletitle',
            name='cl6',
            field=models.CharField(max_length=50, null=True),
        ),
    ]