# Generated by Django 4.2.5 on 2023-11-01 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar_app', '0003_alter_organ_organtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_name', models.CharField(max_length=20)),
                ('own_name', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('ph', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pswd', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('applied', 'Applied')], default='applied', max_length=20)),
            ],
        ),
    ]