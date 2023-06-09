# Generated by Django 3.2.16 on 2023-02-03 23:09

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("client_id", models.IntegerField()),
                ("user_id_mi", models.IntegerField(blank=True, null=True)),
                ("user_id_di", models.IntegerField(blank=True, null=True)),
                ("user_id_wi", models.IntegerField(blank=True, null=True)),
                ("user_id_si", models.IntegerField(blank=True, null=True)),
                ("company_id", models.IntegerField()),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                ("last_ip", models.CharField(blank=True, max_length=40, null=True)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("last_token", models.CharField(blank=True, max_length=64, null=True)),
                ("timestamp_created", models.DateTimeField(blank=True, null=True)),
                ("timestamp_modified", models.DateTimeField(blank=True, null=True)),
                ("firstname", models.CharField(blank=True, max_length=250, null=True)),
                ("lastname", models.CharField(blank=True, max_length=250, null=True)),
                ("timezone", models.CharField(blank=True, max_length=100, null=True)),
                ("email_alerts", models.IntegerField(blank=True, null=True)),
                ("email_activity_alerts", models.IntegerField(blank=True, null=True)),
                ("ent_api_key", models.TextField(blank=True, null=True)),
                ("route", models.CharField(blank=True, max_length=45, null=True)),
                ("is_360", models.IntegerField()),
                ("is_deleted", models.IntegerField(blank=True, null=True)),
                ("is_enabled", models.IntegerField()),
            ],
            options={
                "db_table": "usr_users",
                "managed": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="ClientEdm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("edm_user_id", models.CharField(max_length=15, unique=True)),
                ("ips_client_id", models.IntegerField(blank=True, null=True, unique=True)),
                ("is_deleted", models.IntegerField()),
                ("inserted", models.DateTimeField(blank=True, null=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "usr_clients_edm",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("parent_id", models.IntegerField(blank=True, null=True)),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                "db_table": "usr_roles",
                "managed": False,
            },
        ),
    ]
