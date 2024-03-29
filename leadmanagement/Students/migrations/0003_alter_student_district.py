# Generated by Django 4.2.4 on 2023-09-15 06:22

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('leadmanagementapp', '0005_alter_branche_district'),
        ('Students', '0002_remove_student_state_student_statename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='District',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='statename', chained_model_field='statename', on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.district'),
        ),
    ]
