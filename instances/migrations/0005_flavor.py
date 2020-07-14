# Generated by Django 2.2.13 on 2020-06-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instances', '0004_auto_20200618_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=12, verbose_name='label')),
                ('memory', models.IntegerField(verbose_name='memory')),
                ('vcpu', models.IntegerField(verbose_name='vcpu')),
                ('disk', models.IntegerField(verbose_name='disk')),
            ],
        ),
    ]
