# Generated by Django 4.2.1 on 2023-05-20 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0007_projetrealise_personnels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetrealise',
            name='personnels',
        ),
    ]