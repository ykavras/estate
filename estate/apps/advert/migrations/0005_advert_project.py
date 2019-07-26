# Generated by Django 2.2.2 on 2019-07-26 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_auto_20190727_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='adverts', to='advert.Project', verbose_name='Proje'),
        ),
    ]