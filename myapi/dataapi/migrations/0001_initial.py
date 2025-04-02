# Generated by Django 5.1.7 on 2025-04-02 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGION', models.CharField(max_length=100)),
                ('PROVINCE', models.CharField(max_length=100)),
                ('MUNICIPALITY', models.CharField(max_length=100)),
                ('BARANGAY', models.CharField(max_length=100)),
                ('HH_ID', models.CharField(max_length=50)),
                ('ENTRY_ID', models.CharField(max_length=50, unique=True)),
                ('FIRST_NAME', models.CharField(max_length=100)),
                ('MIDDLE_NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('LAST_NAME', models.CharField(max_length=100)),
                ('EXT_NAME', models.CharField(blank=True, max_length=10, null=True)),
                ('BIRTHDAY', models.DateField()),
                ('AGE', models.IntegerField()),
                ('AGE_ON_EDUC', models.IntegerField()),
                ('SEX', models.CharField(max_length=10)),
                ('MEMBER_STATUS', models.CharField(max_length=50)),
                ('RELATION_TO_HH_HEAD', models.CharField(max_length=100)),
                ('CIVIL_STATUS', models.CharField(max_length=50)),
                ('GRANTEE', models.BooleanField()),
                ('HH_SET', models.CharField(max_length=50)),
                ('SOLOPARENT', models.BooleanField()),
                ('IPAFFILIATION', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
