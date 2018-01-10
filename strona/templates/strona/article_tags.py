from django import template
from strona.models import Post

register = template.Library()

@register.simple_tag
def get_archive_dates():
    
    return Post.objects.only_posts().published().datetimes('created', 'month', order='DESC')
