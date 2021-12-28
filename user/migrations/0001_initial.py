# Generated by Django 4.0 on 2021-12-28 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial', models.TextField(max_length=255)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=125)),
                ('customer_job', models.CharField(max_length=125)),
                ('customer_image', models.ImageField(upload_to='customer/')),
                ('testimonial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.testimonial')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
