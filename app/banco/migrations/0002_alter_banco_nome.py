# Generated by Django 3.2.13 on 2022-06-01 13:18

import banco.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='nome',
            field=models.CharField(max_length=250, unique=True, validators=[banco.validators.nome_validator]),
        ),
    ]
