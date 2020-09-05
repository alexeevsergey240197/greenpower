# Generated by Django 3.0.5 on 2020-09-05 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOfReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименованиe группы отчётов')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электроная почта')),
                ('phone_number', models.TextField(blank=True, max_length=25, verbose_name='Телефонный номер')),
                ('role', models.CharField(blank=True, choices=[('Поручитель отчётности', 'Поручитель отчётности'), ('Субъект отчётности', 'Субъект отчётности'), ('Администратор', 'Администратор')], max_length=30, verbose_name='Роль')),
                ('organisation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_application.Organisation', verbose_name='Организация')),
                ('user', models.OneToOneField(default='default user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Дата создания')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Время последнего обновления')),
                ('status', models.CharField(choices=[('Сформирован', 'Сформирован'), ('Рассматривается', 'Рассматривается'), ('Доработать', 'Доработать'), ('Новый', 'Новый')], max_length=20, verbose_name='Статус')),
                ('context', models.TextField(blank=True, default='', max_length=3000, verbose_name='Контекст таблицы')),
                ('columns', models.IntegerField(default='', verbose_name='Кол-во колонок')),
                ('top_names', models.TextField(blank=True, default='', verbose_name='Имена столбцов')),
                ('message', models.TextField(default='', max_length=600, verbose_name='Приложенное сообщение')),
                ('message_help', models.TextField(blank=True, default='', max_length=600, verbose_name='Сообщение для помощи')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_application.GroupOfReports')),
                ('organisation', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_application.Organisation')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
