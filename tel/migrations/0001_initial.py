# Generated by Django 3.1.5 on 2021-01-08 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11)),
                ('modelo', models.CharField(max_length=20)),
                ('serial', models.CharField(max_length=30)),
                ('imei1', models.CharField(max_length=20)),
                ('imei2', models.CharField(blank=True, max_length=20, null=True)),
                ('setor', models.CharField(max_length=20)),
                ('conta', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=15)),
                ('mac', models.CharField(max_length=17)),
            ],
        ),
    ]
