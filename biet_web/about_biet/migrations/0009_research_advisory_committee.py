# Generated by Django 3.0.8 on 2021-02-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_biet', '0008_major_events_major_events_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research_Advisory_Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=300)),
            ],
        ),
    ]
