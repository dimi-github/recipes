# Generated by Django 3.0.2 on 2020-02-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0025_userpreference_nav_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cors_link',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='link',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]