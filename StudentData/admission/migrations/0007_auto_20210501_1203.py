# Generated by Django 3.1.7 on 2021-05-01 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry_table', '0001_initial'),
        ('admission', '0006_admission_inq_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='inq_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='admission', to='inquiry_table.inquiry'),
        ),
    ]
