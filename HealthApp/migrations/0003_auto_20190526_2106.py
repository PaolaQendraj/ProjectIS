# Generated by Django 2.2.1 on 2019-05-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthApp', '0002_pyetesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pyetesor',
            name='aktiv',
            field=models.CharField(default='humbjepeshe', max_length=100),
        ),
        migrations.AddField(
            model_name='pyetesor',
            name='ditelindja',
            field=models.DateField(default='1998-01-01'),
        ),
        migrations.AddField(
            model_name='pyetesor',
            name='gjinia',
            field=models.CharField(default='humbjepeshe', max_length=100),
        ),
        migrations.AddField(
            model_name='pyetesor',
            name='lloji',
            field=models.CharField(default='humbjepeshe', max_length=100),
        ),
        migrations.AddField(
            model_name='pyetesor',
            name='qellimi',
            field=models.CharField(default='humbjepeshe', max_length=100),
        ),
        migrations.AlterField(
            model_name='pyetesor',
            name='gjatesia',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pyetesor',
            name='pesha',
            field=models.FloatField(),
        ),
    ]