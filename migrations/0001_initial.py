# Generated by Django 3.0.4 on 2020-04-09 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(help_text='Ano dos pedidos, ex: 2020', max_length=4, verbose_name='Ano')),
                ('semestre', models.CharField(help_text='Semestre dos pedidos', max_length=1, verbose_name='Semestre')),
                ('is_active', models.BooleanField(verbose_name='Calendário em vigor')),
                ('inicio_solicitacoes', models.DateField()),
                ('fim_solicitacoes', models.DateField()),
                ('inicio_recursos', models.DateField()),
                ('fim_recursos', models.DateField()),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-ano', '-semestre'],
            },
        ),
        migrations.AddConstraint(
            model_name='calendario',
            constraint=models.UniqueConstraint(fields=('ano', 'semestre'), name='unique_ano_semestre'),
        ),
    ]
