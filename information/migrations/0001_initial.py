# Generated by Django 4.0.4 on 2022-05-22 13:10

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
            name='AnswerInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_information', models.TextField()),
                ('create_date_information', models.DateTimeField()),
                ('modify_date_information', models.DateTimeField(blank=True, null=True)),
                ('author_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_answer_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_information', models.CharField(max_length=200)),
                ('content_information', models.TextField()),
                ('create_date_information', models.DateTimeField()),
                ('modify_date_information', models.DateTimeField(blank=True, null=True)),
                ('author_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_question_information', to=settings.AUTH_USER_MODEL)),
                ('voter_information', models.ManyToManyField(related_name='voter_question_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_information', models.TextField()),
                ('create_date_information', models.DateTimeField()),
                ('modify_date_information', models.DateTimeField(blank=True, null=True)),
                ('answer_information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='information.answerinformation')),
                ('author_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_information', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='information.questioninformation')),
            ],
        ),
        migrations.AddField(
            model_name='answerinformation',
            name='question_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.questioninformation'),
        ),
        migrations.AddField(
            model_name='answerinformation',
            name='voter_information',
            field=models.ManyToManyField(related_name='voter_answer_information', to=settings.AUTH_USER_MODEL),
        ),
    ]
