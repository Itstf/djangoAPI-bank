# Generated by Django 4.1.1 on 2022-09-26 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_imagens'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartao',
            old_name='tipoCartão',
            new_name='tipoCartao',
        ),
    ]
