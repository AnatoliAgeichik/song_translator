# Generated by Django 3.2 on 2021-05-14 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('original_language', models.CharField(choices=[('af', 'afrikaans'), ('sq', 'albanian'), ('am', 'amharic'), ('ar', 'arabic'), ('hy', 'armenian'), ('az', 'azerbaijani'), ('eu', 'basque'), ('be', 'belarusian'), ('bn', 'bengali'), ('bs', 'bosnian'), ('bg', 'bulgarian'), ('ca', 'catalan'), ('ny', 'chichewa'), ('co', 'corsican'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('nl', 'dutch'), ('en', 'english'), ('eo', 'esperanto'), ('et', 'estonian'), ('tl', 'filipino'), ('fi', 'finnish'), ('fr', 'french'), ('fy', 'frisian'), ('gl', 'galician'), ('ka', 'georgian'), ('de', 'german'), ('el', 'greek'), ('gu', 'gujarati'), ('ht', 'haitian creole'), ('ha', 'hausa'), ('iw', 'hebrew'), ('he', 'hebrew'), ('hi', 'hindi'), ('hu', 'hungarian'), ('is', 'icelandic'), ('ig', 'igbo'), ('id', 'indonesian'), ('ga', 'irish'), ('it', 'italian'), ('ja', 'japanese'), ('jw', 'javanese'), ('kn', 'kannada'), ('kk', 'kazakh'), ('km', 'khmer'), ('ko', 'korean'), ('ku', 'kurdish (kurmanji)'), ('ky', 'kyrgyz'), ('lo', 'lao'), ('la', 'latin'), ('lv', 'latvian'), ('lt', 'lithuanian'), ('lb', 'luxembourgish'), ('mk', 'macedonian'), ('mg', 'malagasy'), ('ms', 'malay'), ('ml', 'malayalam'), ('mt', 'maltese'), ('mi', 'maori'), ('mr', 'marathi'), ('mn', 'mongolian'), ('my', 'myanmar (burmese)'), ('ne', 'nepali'), ('no', 'norwegian'), ('or', 'odia'), ('ps', 'pashto'), ('fa', 'persian'), ('pl', 'polish'), ('pt', 'portuguese'), ('pa', 'punjabi'), ('ro', 'romanian'), ('ru', 'russian'), ('sm', 'samoan'), ('gd', 'scots gaelic'), ('sr', 'serbian'), ('st', 'sesotho'), ('sn', 'shona'), ('sd', 'sindhi'), ('si', 'sinhala'), ('sk', 'slovak'), ('sl', 'slovenian'), ('so', 'somali'), ('es', 'spanish'), ('su', 'sundanese'), ('sw', 'swahili'), ('sv', 'swedish'), ('tg', 'tajik'), ('ta', 'tamil'), ('te', 'telugu'), ('th', 'thai'), ('tr', 'turkish'), ('tk', 'turkmen'), ('uk', 'ukrainian'), ('ur', 'urdu'), ('ug', 'uyghur'), ('uz', 'uzbek'), ('vi', 'vietnamese'), ('cy', 'welsh'), ('xh', 'xhosa'), ('yi', 'yiddish'), ('yo', 'yoruba'), ('zu', 'zulu')], default='en', max_length=2)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL)),
                ('singer', models.ManyToManyField(to='track.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('language', models.CharField(choices=[('af', 'afrikaans'), ('sq', 'albanian'), ('am', 'amharic'), ('ar', 'arabic'), ('hy', 'armenian'), ('az', 'azerbaijani'), ('eu', 'basque'), ('be', 'belarusian'), ('bn', 'bengali'), ('bs', 'bosnian'), ('bg', 'bulgarian'), ('ca', 'catalan'), ('ny', 'chichewa'), ('co', 'corsican'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('nl', 'dutch'), ('en', 'english'), ('eo', 'esperanto'), ('et', 'estonian'), ('tl', 'filipino'), ('fi', 'finnish'), ('fr', 'french'), ('fy', 'frisian'), ('gl', 'galician'), ('ka', 'georgian'), ('de', 'german'), ('el', 'greek'), ('gu', 'gujarati'), ('ht', 'haitian creole'), ('ha', 'hausa'), ('iw', 'hebrew'), ('he', 'hebrew'), ('hi', 'hindi'), ('hu', 'hungarian'), ('is', 'icelandic'), ('ig', 'igbo'), ('id', 'indonesian'), ('ga', 'irish'), ('it', 'italian'), ('ja', 'japanese'), ('jw', 'javanese'), ('kn', 'kannada'), ('kk', 'kazakh'), ('km', 'khmer'), ('ko', 'korean'), ('ku', 'kurdish (kurmanji)'), ('ky', 'kyrgyz'), ('lo', 'lao'), ('la', 'latin'), ('lv', 'latvian'), ('lt', 'lithuanian'), ('lb', 'luxembourgish'), ('mk', 'macedonian'), ('mg', 'malagasy'), ('ms', 'malay'), ('ml', 'malayalam'), ('mt', 'maltese'), ('mi', 'maori'), ('mr', 'marathi'), ('mn', 'mongolian'), ('my', 'myanmar (burmese)'), ('ne', 'nepali'), ('no', 'norwegian'), ('or', 'odia'), ('ps', 'pashto'), ('fa', 'persian'), ('pl', 'polish'), ('pt', 'portuguese'), ('pa', 'punjabi'), ('ro', 'romanian'), ('ru', 'russian'), ('sm', 'samoan'), ('gd', 'scots gaelic'), ('sr', 'serbian'), ('st', 'sesotho'), ('sn', 'shona'), ('sd', 'sindhi'), ('si', 'sinhala'), ('sk', 'slovak'), ('sl', 'slovenian'), ('so', 'somali'), ('es', 'spanish'), ('su', 'sundanese'), ('sw', 'swahili'), ('sv', 'swedish'), ('tg', 'tajik'), ('ta', 'tamil'), ('te', 'telugu'), ('th', 'thai'), ('tr', 'turkish'), ('tk', 'turkmen'), ('uk', 'ukrainian'), ('ur', 'urdu'), ('ug', 'uyghur'), ('uz', 'uzbek'), ('vi', 'vietnamese'), ('cy', 'welsh'), ('xh', 'xhosa'), ('yi', 'yiddish'), ('yo', 'yoruba'), ('zu', 'zulu')], default='en', max_length=2)),
                ('auto_translate', models.BooleanField(default=True)),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translate_track', to='track.track')),
            ],
        ),
    ]
