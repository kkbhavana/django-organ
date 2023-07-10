# Generated by Django 4.2.2 on 2023-07-07 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('o_donation', '0002_doner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('status', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]