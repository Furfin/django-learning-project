# Generated by Django 3.2.3 on 2021-05-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comment_delete',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]