# Generated by Django 2.1 on 2018-10-14 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0010_auto_20181002_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medias',
            fields=[
                ('posicao', models.CharField(max_length=20)),
                ('idPosicao', models.IntegerField(primary_key=True, serialize=False)),
                ('quarentaJardas', models.DecimalField(decimal_places=3, max_digits=5)),
                ('supino', models.IntegerField()),
                ('saltoVertical', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saltoHorizontal', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='atletas',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]