# Generated by Django 3.2 on 2021-05-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='translate',
            name='track_translate_LangType_valid',
        ),
        migrations.AlterField(
            model_name='track',
            name='original_language',
            field=models.CharField(choices=[('af', 'afrikaans'), ('sq', 'albanian'), ('am', 'amharic'), ('ar', 'arabic'), ('hy', 'armenian'), ('az', 'azerbaijani'), ('eu', 'basque'), ('be', 'belarusian'), ('bn', 'bengali'), ('bs', 'bosnian'), ('bg', 'bulgarian'), ('ca', 'catalan'), ('ny', 'chichewa'), ('co', 'corsican'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('nl', 'dutch'), ('en', 'english'), ('eo', 'esperanto'), ('et', 'estonian'), ('tl', 'filipino'), ('fi', 'finnish'), ('fr', 'french'), ('fy', 'frisian'), ('gl', 'galician'), ('ka', 'georgian'), ('de', 'german'), ('el', 'greek'), ('gu', 'gujarati'), ('ht', 'haitian creole'), ('ha', 'hausa'), ('iw', 'hebrew'), ('he', 'hebrew'), ('hi', 'hindi'), ('hu', 'hungarian'), ('is', 'icelandic'), ('ig', 'igbo'), ('id', 'indonesian'), ('ga', 'irish'), ('it', 'italian'), ('ja', 'japanese'), ('jw', 'javanese'), ('kn', 'kannada'), ('kk', 'kazakh'), ('km', 'khmer'), ('ko', 'korean'), ('ku', 'kurdish (kurmanji)'), ('ky', 'kyrgyz'), ('lo', 'lao'), ('la', 'latin'), ('lv', 'latvian'), ('lt', 'lithuanian'), ('lb', 'luxembourgish'), ('mk', 'macedonian'), ('mg', 'malagasy'), ('ms', 'malay'), ('ml', 'malayalam'), ('mt', 'maltese'), ('mi', 'maori'), ('mr', 'marathi'), ('mn', 'mongolian'), ('my', 'myanmar (burmese)'), ('ne', 'nepali'), ('no', 'norwegian'), ('or', 'odia'), ('ps', 'pashto'), ('fa', 'persian'), ('pl', 'polish'), ('pt', 'portuguese'), ('pa', 'punjabi'), ('ro', 'romanian'), ('ru', 'russian'), ('sm', 'samoan'), ('gd', 'scots gaelic'), ('sr', 'serbian'), ('st', 'sesotho'), ('sn', 'shona'), ('sd', 'sindhi'), ('si', 'sinhala'), ('sk', 'slovak'), ('sl', 'slovenian'), ('so', 'somali'), ('es', 'spanish'), ('su', 'sundanese'), ('sw', 'swahili'), ('sv', 'swedish'), ('tg', 'tajik'), ('ta', 'tamil'), ('te', 'telugu'), ('th', 'thai'), ('tr', 'turkish'), ('tk', 'turkmen'), ('uk', 'ukrainian'), ('ur', 'urdu'), ('ug', 'uyghur'), ('uz', 'uzbek'), ('vi', 'vietnamese'), ('cy', 'welsh'), ('xh', 'xhosa'), ('yi', 'yiddish'), ('yo', 'yoruba'), ('zu', 'zulu')], default='en', max_length=2),
        ),
        migrations.AlterField(
            model_name='translate',
            name='language',
            field=models.CharField(choices=[('af', 'afrikaans'), ('sq', 'albanian'), ('am', 'amharic'), ('ar', 'arabic'), ('hy', 'armenian'), ('az', 'azerbaijani'), ('eu', 'basque'), ('be', 'belarusian'), ('bn', 'bengali'), ('bs', 'bosnian'), ('bg', 'bulgarian'), ('ca', 'catalan'), ('ny', 'chichewa'), ('co', 'corsican'), ('hr', 'croatian'), ('cs', 'czech'), ('da', 'danish'), ('nl', 'dutch'), ('en', 'english'), ('eo', 'esperanto'), ('et', 'estonian'), ('tl', 'filipino'), ('fi', 'finnish'), ('fr', 'french'), ('fy', 'frisian'), ('gl', 'galician'), ('ka', 'georgian'), ('de', 'german'), ('el', 'greek'), ('gu', 'gujarati'), ('ht', 'haitian creole'), ('ha', 'hausa'), ('iw', 'hebrew'), ('he', 'hebrew'), ('hi', 'hindi'), ('hu', 'hungarian'), ('is', 'icelandic'), ('ig', 'igbo'), ('id', 'indonesian'), ('ga', 'irish'), ('it', 'italian'), ('ja', 'japanese'), ('jw', 'javanese'), ('kn', 'kannada'), ('kk', 'kazakh'), ('km', 'khmer'), ('ko', 'korean'), ('ku', 'kurdish (kurmanji)'), ('ky', 'kyrgyz'), ('lo', 'lao'), ('la', 'latin'), ('lv', 'latvian'), ('lt', 'lithuanian'), ('lb', 'luxembourgish'), ('mk', 'macedonian'), ('mg', 'malagasy'), ('ms', 'malay'), ('ml', 'malayalam'), ('mt', 'maltese'), ('mi', 'maori'), ('mr', 'marathi'), ('mn', 'mongolian'), ('my', 'myanmar (burmese)'), ('ne', 'nepali'), ('no', 'norwegian'), ('or', 'odia'), ('ps', 'pashto'), ('fa', 'persian'), ('pl', 'polish'), ('pt', 'portuguese'), ('pa', 'punjabi'), ('ro', 'romanian'), ('ru', 'russian'), ('sm', 'samoan'), ('gd', 'scots gaelic'), ('sr', 'serbian'), ('st', 'sesotho'), ('sn', 'shona'), ('sd', 'sindhi'), ('si', 'sinhala'), ('sk', 'slovak'), ('sl', 'slovenian'), ('so', 'somali'), ('es', 'spanish'), ('su', 'sundanese'), ('sw', 'swahili'), ('sv', 'swedish'), ('tg', 'tajik'), ('ta', 'tamil'), ('te', 'telugu'), ('th', 'thai'), ('tr', 'turkish'), ('tk', 'turkmen'), ('uk', 'ukrainian'), ('ur', 'urdu'), ('ug', 'uyghur'), ('uz', 'uzbek'), ('vi', 'vietnamese'), ('cy', 'welsh'), ('xh', 'xhosa'), ('yi', 'yiddish'), ('yo', 'yoruba'), ('zu', 'zulu')], default='en', max_length=2),
        ),
    ]
