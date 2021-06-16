# Generated by Django 3.1.6 on 2021-04-12 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='img/%y')),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.loja')),
            ],
        ),
    ]
