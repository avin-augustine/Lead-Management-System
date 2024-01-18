# Generated by Django 4.2.4 on 2023-09-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0004_rename_statename_student_statename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Registration_No',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Year_of_pass',
            field=models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='qualification',
            field=models.CharField(choices=[('BE', 'BE'), ('B.Tech', 'B.Tech')], max_length=50),
        ),
    ]
