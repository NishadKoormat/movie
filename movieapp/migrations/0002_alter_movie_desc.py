# Generated by Django 4.2.5 on 2023-10-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(),
        ),
    ]
