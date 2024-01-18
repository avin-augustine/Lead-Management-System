# Generated by Django 4.2.4 on 2023-09-13 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Companie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('address3', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(max_length=30)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='upload_photos')),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enquirysourcename', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow_up_statuse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Followupstatusname', models.CharField(max_length=250)),
                ('Followupstatus', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Master_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Value', models.CharField(max_length=25)),
                ('Type', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qualificationame', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statename', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Syllabus', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=25)),
                ('Coursecode', models.CharField(max_length=25)),
                ('Trainers', models.CharField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
                ('available_trainers', models.ManyToManyField(related_name='available_courses', to=settings.AUTH_USER_MODEL)),
                ('chosen_trainers', models.ManyToManyField(related_name='chosen_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Branche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch', models.CharField(max_length=25)),
                ('Branch_code', models.CharField(max_length=25)),
                ('adress', models.CharField(max_length=25)),
                ('Street', models.CharField(max_length=25)),
                ('Pincode', models.CharField(max_length=25)),
                ('Mobile', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=25)),
                ('Active', models.BooleanField(default=True)),
                ('district', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.district')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.state')),
            ],
        ),
    ]
