from django.db import models

from django.utils import timezone


class Category(models.Model):
    name = models.CharField('Nazwa Kategorii', max_length=100)
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)
    icon = models.ImageField('Ikonka Kategorii', upload_to='icons',
                              blank=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __unicode__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField('Tytuł', max_length=200)
    text = models.TextField()
    categories = models.ManyToManyField(Category, verbose_name='Kategorie')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
