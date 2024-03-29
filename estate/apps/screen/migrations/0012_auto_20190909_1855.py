# Generated by Django 2.2.2 on 2019-09-09 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0011_auto_20190704_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotspot',
            name='target_screen',
            field=models.ForeignKey(blank=True, help_text='Sadece tip "scene" ise doldurunuz', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_links', to='screen.Screen', verbose_name='Hedef Ekran'),
        ),
        migrations.AlterField(
            model_name='hotspot',
            name='screen',
            field=models.ForeignKey(help_text='Hangi ekranda gösterilecek', on_delete=django.db.models.deletion.CASCADE, related_name='hotspots', to='screen.Screen'),
        ),
    ]
