import factory
from faker import Factory as FakerFactory
from . import models

faker = FakerFactory.create()


class ArtistsFactory(factory.django.DjangoModelFactory):
    """Author factory."""

    name = faker.name()
    aritsts_images = faker.image_url()
    aritsts_uri = faker.url()

    class Meta:
        model = models.artists
        



# class BookFactory(factory.django.DjangoModelFactory):
#     """Book factory."""

#     title = faker.sentence(nb_words=4)

#     class Meta:
#         model = models.Book

#     # author = factory.SubFactory(AuthorFactory)

