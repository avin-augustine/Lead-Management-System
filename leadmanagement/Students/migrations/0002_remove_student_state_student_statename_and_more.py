# Generated by Django 4.2.4 on 2023-09-15 06:19

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('leadmanagementapp', '0005_alter_branche_district'),
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='state',
        ),
        migrations.AddField(
            model_name='student',
            name='statename',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.state'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='District',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='Statename', chained_model_field='Statename', on_delete=django.db.models.deletion.CASCADE, to='leadmanagementapp.district'),
        ),
        migrations.AlterField(
            model_name='student',
            name='enquiry_source',
            field=models.CharField(choices=[('Website', 'Website'), ('Advertisement', 'Advertisement'), ('Friend', 'Friend')], max_length=50),
        ),
    ]
