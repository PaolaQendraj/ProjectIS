# Generated by Django 2.2.1 on 2019-06-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0009_darka_dreka_snacks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktiviteti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri', models.CharField(max_length=50)),
                ('koeficienti', models.FloatField()),
                ('foto', models.ImageField(upload_to='media')),
            ],
        ),
    ]
