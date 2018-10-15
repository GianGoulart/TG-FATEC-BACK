# Generated by Django 2.1 on 2018-10-02 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0008_skills_dataavaliacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('nome', models.CharField(max_length=50)),
                ('quarentaJardas', models.DecimalField(decimal_places=3, max_digits=5)),
                ('supino', models.IntegerField()),
                ('saltoVertical', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saltoHorizontal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('idAtleta', models.IntegerField(primary_key=True, serialize=False)),
                ('dataAvaliacao', models.DateTimeField()),
            ],
        ),
    ]