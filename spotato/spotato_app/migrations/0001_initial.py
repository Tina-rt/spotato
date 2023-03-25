# Generated by Django 4.1.7 on 2023-03-25 15:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('date_time', models.DateTimeField(default=datetime.datetime(2023, 3, 25, 16, 45, 29, 623920))),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_transaction_destination', to=settings.AUTH_USER_MODEL)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_transaction_source', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spotter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('duration', models.FloatField()),
                ('requested_start_time', models.DateTimeField()),
                ('montant', models.FloatField()),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='spotato_app.categorie')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='spotato_app.client')),
                ('spotter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotato_app.spotter')),
            ],
        ),
    ]