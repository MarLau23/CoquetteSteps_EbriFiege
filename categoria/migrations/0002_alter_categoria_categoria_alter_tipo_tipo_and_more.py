# Generated by Django 5.0.4 on 2024-06-20 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='tipo',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='tipo',
            unique_together={('categoria_nom', 'tipo')},
        ),
    ]
