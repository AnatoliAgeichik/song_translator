import factory.fuzzy

from .models import Singer, Track, Translation, Comment
from .utils import get_random_lang_for_factory


class SingerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Singer
    name = factory.Faker("name")


class TrackFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Track

    track_name = factory.Faker("word", locale=get_random_lang_for_factory(new_value=True))
    text = factory.Faker("text", locale=get_random_lang_for_factory(new_value=False))
    original_language = get_random_lang_for_factory(new_value=False)

    @factory.post_generation
    def singer(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for sing in extracted:
                self.singer.add(sing)
        else:
            sing = SingerFactory()
            self.singer.add(sing)


class TranslationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Translation
    track_id = factory.SubFactory(TrackFactory)
    text = factory.Faker("text", locale=get_random_lang_for_factory(new_value=True))
    language = get_random_lang_for_factory(new_value=False)
    auto_translate = False


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment
    track_id = factory.SubFactory(TrackFactory)
    message = factory.Faker("text")
    mark = factory.fuzzy.FuzzyInteger(1, 5)
