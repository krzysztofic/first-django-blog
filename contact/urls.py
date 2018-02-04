from django.conf.urls import url
from . import views
from contact.views import MessageAddView



app_name = 'contact'

urlpatterns = [
    url(r'^blog/contact/$', MessageAddView.as_view(), name='blog_message'),
]
