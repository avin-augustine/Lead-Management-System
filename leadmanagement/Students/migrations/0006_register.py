# Generated by Django 4.2.4 on 2023-09-21 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leadmanagementapp', '0005_alter_branche_district'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Students', '0005_student_registration_no_student_year_of_pass_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='Email')),
                ('batch', models.CharField(max_length=200, verbose_name='Batch')),
                ('have_laptop', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, verbose_name='Do you have laptop')),
                ('isactive', models.BooleanField(default=True, verbose_name='Registered')),
                ('course', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.course', verbose_name='Course')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Students.student')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Trainer')),
            ],
        ),
    ]
