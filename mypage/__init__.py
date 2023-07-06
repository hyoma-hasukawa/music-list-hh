import factory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class AuthorFactory(factory.django.DjangoModelFactory):
    """Author factory."""

    name = factory.LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'app.Author'


class BookFactory(factory.django.DjangoModelFactory):
    """Book factory."""

    title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=4))

    class Meta:
        model = 'app.Book'

    author = factory.SubFactory(AuthorFactory)