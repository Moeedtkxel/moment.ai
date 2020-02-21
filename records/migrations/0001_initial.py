# Generated by Django 3.0.3 on 2020-02-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_id', models.IntegerField()),
                ('frame_name', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('pose_yaw', models.FloatField()),
                ('pose_pitch', models.FloatField()),
                ('pose_roll', models.FloatField()),
                ('face_status', models.CharField(max_length=255)),
            ],
        ),
    ]
