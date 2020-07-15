# Generated by Django 3.0.8 on 2020-07-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0008_auto_20200715_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio_medical_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='bio_technology_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='chemical_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='chemistry_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='civil_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='computer_science_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='electrical_and_electronics_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='electronics_and_communication_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='electronics_and_instrumentation_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='information_science_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='mathematics_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='mechanical_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='physics_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
        migrations.AddField(
            model_name='textile_technology_dept',
            name='description',
            field=models.TextField(blank=True, help_text='Enter description only for HOD. For others this field can be skipped.'),
        ),
    ]
