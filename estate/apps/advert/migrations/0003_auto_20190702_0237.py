# Generated by Django 2.2.2 on 2019-07-01 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_auto_20190702_0232'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PropertTitle',
            new_name='PropertyTitle',
        ),
        migrations.AddField(
            model_name='property',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='advert.PropertyTitle', verbose_name='Ana Başlık'),
            preserve_default=False,
        ),
    ]
