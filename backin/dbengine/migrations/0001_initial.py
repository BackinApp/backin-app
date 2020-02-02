# Generated by Django 2.2.9 on 2020-02-02 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DBEngines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('code_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('display_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('oficial_doc', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_change', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
