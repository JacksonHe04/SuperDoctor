# Generated by Django 5.1 on 2024-10-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestSet",
            fields=[
                ("auto_id", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.IntegerField(blank=True, null=True)),
                ("sentence", models.TextField(blank=True, null=True)),
                ("h", models.CharField(blank=True, max_length=255, null=True)),
                ("t", models.CharField(blank=True, max_length=255, null=True)),
                ("r", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "test",
            },
        ),
        migrations.CreateModel(
            name="TrainSet",
            fields=[
                ("auto_id", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.IntegerField(blank=True, null=True)),
                ("sentence", models.TextField(blank=True, null=True)),
                ("h", models.CharField(blank=True, max_length=255, null=True)),
                ("t", models.CharField(blank=True, max_length=255, null=True)),
                ("r", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "train",
            },
        ),
        migrations.CreateModel(
            name="ValSet",
            fields=[
                ("auto_id", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.IntegerField(blank=True, null=True)),
                ("sentence", models.TextField(blank=True, null=True)),
                ("h", models.CharField(blank=True, max_length=255, null=True)),
                ("t", models.CharField(blank=True, max_length=255, null=True)),
                ("r", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "val",
            },
        ),
    ]
