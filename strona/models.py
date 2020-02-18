from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet

from django.utils import timezone
from model_utils import Choices
from model_utils.models import StatusModel


class PostQuerySet(QuerySet):
    def published(self):
        return self.filter(status='published')

    def draft(self):
        return self.filter(status='draft')


class Category(models.Model):
    name = models.CharField('Nazwa Kategorii', max_length=100)


    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name

class Post(StatusModel):
    STATUS = Choices(
        ('draft', ("draft")),
        ('published', ("published")),
    )

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Tytuł', max_length=200)
    slug = models.SlugField('Odnośnik', max_length=100, unique=True)
    lead = models.TextField('Wstęp', null=True)
    text = models.TextField()
    categories = models.ManyToManyField(Category, verbose_name='Kategorie')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostQuerySet.as_manager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post_details', [], {'slug': self.slug})
