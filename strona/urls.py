from django.conf.urls import url
from . import views
from .views import PostView, PostMonthArchiveView, PostDetailsView

app_name = 'strona'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', PostView.as_view(), name='post_View'),
    # url(r'^$', PostView.as_view(), name='post_View'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$',PostMonthArchiveView.as_view(), name='month_archive'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailsView.as_view(), name='post_details'),
]
