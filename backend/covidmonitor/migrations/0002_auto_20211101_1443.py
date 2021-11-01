# Generated by Django 3.2.7 on 2021-11-01 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidmonitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidMonitorDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('time_series_num', models.IntegerField(blank=True, null=True)),
                ('daily_reports_num', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='covidmonitor.country')),
                ('province_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='covidmonitor.provincestate')),
            ],
        ),
        migrations.RemoveField(
            model_name='confirmed',
            name='country',
        ),
        migrations.RemoveField(
            model_name='confirmed',
            name='province_state',
        ),
        migrations.RemoveField(
            model_name='deaths',
            name='country',
        ),
        migrations.RemoveField(
            model_name='deaths',
            name='province_state',
        ),
        migrations.RemoveField(
            model_name='recovered',
            name='country',
        ),
        migrations.RemoveField(
            model_name='recovered',
            name='province_state',
        ),
        migrations.DeleteModel(
            name='Active',
        ),
        migrations.DeleteModel(
            name='Confirmed',
        ),
        migrations.DeleteModel(
            name='Deaths',
        ),
        migrations.DeleteModel(
            name='Recovered',
        ),
    ]