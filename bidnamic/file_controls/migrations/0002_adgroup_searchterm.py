# Generated by Django 3.2.12 on 2022-03-20 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_controls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, max_length=250, null=True, verbose_name='Alias')),
                ('status', models.CharField(blank=True, max_length=250, null=True, verbose_name='Status')),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='file_controls.campaign', verbose_name='Connected Campaign')),
            ],
            options={
                'verbose_name': 'AdGroup',
                'verbose_name_plural': 'AdGroups',
            },
        ),
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('click', models.IntegerField(blank=True, null=True, verbose_name='Click Amount')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Click Amount')),
                ('conversion_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Conversion Value')),
                ('conversion', models.IntegerField(blank=True, null=True, verbose_name='Conversion')),
                ('search_term', models.CharField(blank=True, max_length=250, null=True, verbose_name='Search Term')),
                ('ad_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='file_controls.adgroup', verbose_name='Connected Ad Group')),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='file_controls.campaign', verbose_name='Connected Campaign')),
            ],
            options={
                'verbose_name': 'Search Term',
                'verbose_name_plural': 'Search Terms',
            },
        ),
    ]
