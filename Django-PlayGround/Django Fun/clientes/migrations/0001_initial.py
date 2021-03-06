# Generated by Django 4.0.3 on 2022-04-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("online", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("rg", models.CharField(max_length=9)),
                ("celular", models.CharField(max_length=14)),
                ("avatar", models.ImageField(upload_to="avatar")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
