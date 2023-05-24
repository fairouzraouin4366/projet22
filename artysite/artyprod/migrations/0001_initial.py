# Generated by Django 4.2.1 on 2023-05-07 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('date_naissance', models.DateField(null=True)),
                ('fichier_cv', models.FileField(blank=True, null=True, upload_to='media/cv/')),
                ('fichier_photo', models.ImageField(blank=True, null=True, upload_to='media/photo')),
                ('fichier_linkedln', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('dg', 'design graphique'), ('pa', 'production audiovisuelle'), ('3D', 'Conception 3D')], default='', max_length=2)),
                ('description', models.TextField(default='non définie')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellé', models.CharField(max_length=100)),
                ('description', models.TextField(default='non définie')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('achevée', models.CharField(choices=[('o', 'acheve'), ('n', 'en cours')], max_length=2)),
                ('equipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artyprod.equipe')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artyprod.service')),
            ],
        ),
        migrations.AddField(
            model_name='equipe',
            name='personnel',
            field=models.ManyToManyField(to='artyprod.personnel'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.ImageField(blank=True, null=True, upload_to='media/fichier')),
                ('Projet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artyprod.projet')),
                ('Service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artyprod.service')),
            ],
        ),
    ]