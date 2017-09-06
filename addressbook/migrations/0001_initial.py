# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created',
                 django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified',
                 django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('contact_name', models.CharField(max_length=50, verbose_name='contact name')),
                ('address_one', models.CharField(max_length=50, verbose_name='address one')),
                ('address_two', models.CharField(blank=True, max_length=50, verbose_name='address two')),
                ('town', models.CharField(max_length=50, verbose_name='town')),
                ('county', models.CharField(blank=True, max_length=50, verbose_name='county')),
                ('postcode', models.CharField(max_length=50, verbose_name='postcode')),
                ('status',
                 models.IntegerField(choices=[(0, b'Active'), (1, b'Display only'), (2, b'Deleted')], default=0,
                                     verbose_name='status')),
            ],
            options={
                'ordering': ['created'],
                'get_latest_by': 'created',
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=2, unique=True, verbose_name='ISO code')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addressbook.Country',
                                    verbose_name='country'),
        ),
    ]
