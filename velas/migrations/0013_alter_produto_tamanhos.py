# Generated by Django 5.0.8 on 2024-12-11 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velas', '0012_alter_produto_tamanhos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tamanhos',
            field=models.ManyToManyField(related_name='produto', to='velas.tamanho'),
        ),
    ]