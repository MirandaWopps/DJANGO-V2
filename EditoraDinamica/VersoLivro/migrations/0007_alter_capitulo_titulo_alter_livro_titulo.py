# Generated by Django 5.1.1 on 2024-10-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VersoLivro', '0006_alter_livro_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='titulo',
            field=models.CharField(help_text='nome', max_length=30),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(help_text='nome', max_length=100),
        ),
    ]
