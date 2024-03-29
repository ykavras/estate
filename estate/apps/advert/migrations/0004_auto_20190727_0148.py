# Generated by Django 2.2.2 on 2019-07-26 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_auto_20190702_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Adı')),
                ('main_image', models.ImageField(upload_to='projects/main_image/', verbose_name='Resim')),
                ('description', models.TextField(verbose_name='Açıklama')),
            ],
            options={
                'verbose_name': 'Proje',
                'verbose_name_plural': 'Projeler',
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='image_detail',
            field=models.ImageField(default='projects/galeri/1.jpg', upload_to='advert/galeri/', verbose_name='Detay Sayfası İçin Resim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advert',
            name='image_list',
            field=models.ImageField(default='projects/gallery/2.jpg', upload_to='advert/galeri/', verbose_name='Listeleme Sayfası İçin Resim'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='advert/galeri/', verbose_name='Resim')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='advert.Advert', verbose_name='İlan')),
            ],
            options={
                'verbose_name': 'Galeri',
                'verbose_name_plural': 'Galeri',
            },
        ),
    ]
