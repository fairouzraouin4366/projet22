# Generated by Django 4.2.1 on 2023-05-20 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0010_rename_fichier_cv_personnel_cvprs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='cvprs',
            new_name='cvPrs',
        ),
        migrations.RenameField(
            model_name='personnel',
            old_name='photoprs',
            new_name='photoPrs',
        ),
    ]