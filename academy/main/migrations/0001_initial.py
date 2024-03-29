# Generated by Django 5.0 on 2024-01-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('whatsapp_number', models.CharField(max_length=15)),
                ('occupation', models.CharField(max_length=100)),
                ('preferred_exam', models.CharField(choices=[('tnpsc_group1', 'TNPSC Group 1'), ('tnpsc_group4', 'TNPSC Group 4'), ('tnusrp_si', 'TNUSRP SI Open Quota'), ('bc_exam', 'BC Exam')], max_length=50)),
            ],
        ),
    ]
