# Generated by Django 3.1.3 on 2021-04-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RAG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Residents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forename', models.TextField()),
                ('middle_names', models.TextField(blank=True)),
                ('surname', models.TextField()),
                ('dob', models.DateField()),
                ('previous_address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schemes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OPP',
            fields=[
                ('resident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='scone_backend_django_rest.residents')),
                ('t1', models.TextField()),
                ('t2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entries', models.TextField()),
                ('resident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scone_backend_django_rest.residents')),
            ],
        ),
        migrations.CreateModel(
            name='Risks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.TextField()),
                ('mitigation', models.TextField()),
                ('rag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scone_backend_django_rest.rag')),
                ('resident_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scone_backend_django_rest.residents')),
            ],
        ),
        migrations.AddField(
            model_name='residents',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scone_backend_django_rest.schemes'),
        ),
    ]