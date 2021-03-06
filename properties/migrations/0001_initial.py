# Generated by Django 4.0.3 on 2022-05-23 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Agency',
                'verbose_name_plural': 'Agencies',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('type', models.CharField(max_length=250)),
                ('area', models.CharField(default=1, max_length=13)),
                ('bedrooms', models.CharField(default=1, max_length=13)),
                ('total_units', models.CharField(max_length=13)),
                ('occupied_units', models.CharField(max_length=13)),
                ('unoccupied_units', models.CharField(max_length=13)),
                ('landlord', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.landlord')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('period', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('amountDue', models.CharField(blank=True, max_length=250, null=True)),
                ('landlord', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.landlord')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.property')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.tenant')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.tenant'),
        ),
    ]
