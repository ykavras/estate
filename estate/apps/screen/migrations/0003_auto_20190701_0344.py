# Generated by Django 2.2.2 on 2019-07-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0002_auto_20190701_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotspot',
            name='screenid',
            field=models.CharField(blank=True, help_text='If type is screen fill here', max_length=255, null=True, verbose_name='Screen Id'),
        ),
        migrations.AddField(
            model_name='hotspot',
            name='type',
            field=models.CharField(choices=[('info', 'info'), ('scene', 'scene')], default='screen', max_length=5, verbose_name='Types'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotspot',
            name='text',
            field=models.CharField(blank=True, help_text='If type is info fill here', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hotspot',
            name='url',
            field=models.URLField(blank=True, help_text='If type is info then you may give link', null=True),
        ),
    ]