# Generated by Django 5.2 on 2025-04-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('BR', 'Brazilian'), ('US', 'American'), ('UK', 'British'), ('FR', 'French'), ('DE', 'German'), ('JP', 'Japanese'), ('IT', 'Italian'), ('ES', 'Spanish'), ('CN', 'Chinese'), ('IN', 'Indian'), ('RU', 'Russian'), ('KR', 'South Korean'), ('MX', 'Mexican'), ('CA', 'Canadian'), ('AU', 'Australian'), ('ZA', 'South African')], max_length=100, null=True)),
            ],
        ),
    ]
