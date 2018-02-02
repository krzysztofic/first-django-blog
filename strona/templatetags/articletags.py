from django import template
from strona.models import Post

register = template.Library()


@register.assignment_tag
def get_archive_dates():

    return Post.objects.published().datetimes('created_date', 'month', order='DESC')

@register.assignment_tag
def get_related_posts(post, count=5):

    return Post.objects.published().order_by('-created_date')[:count]
