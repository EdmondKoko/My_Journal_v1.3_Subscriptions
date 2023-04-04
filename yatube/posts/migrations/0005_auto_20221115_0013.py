# Generated by Django 2.2.16 on 2022-11-14 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20221112_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Обязательное поле, не должно быть пустым', verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Дата публикации', verbose_name='Дата публикации')),
                ('author', models.ForeignKey(help_text='Автор отображается на сайте', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('post', models.ForeignKey(help_text='Под каким постом оставлен комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post', verbose_name='Пост')),
            ],
            options={
                'verbose_name_plural': 'Комментарии к постам',
                'ordering': ('-created',),
            },
        ),
    ]
