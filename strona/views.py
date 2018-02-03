from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, MonthArchiveView

from django.shortcuts import render_to_response
from django.template import RequestContext

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.published().order_by('-created_date')
    paginator = Paginator(posts, 3)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)


    return render(request, 'strona/post_list.html', {'posts': posts})


class PostView(ListView):
    template_name = "strona/templates/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context['published'] = Post.objects.published()
        return context


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.published()
    date_field = 'created_date'
    month_format = '%m'
    make_object_list = True


class PostDetailsView(DetailView):

    def get_queryset(self):
        return Post.objects.published()

    def get_object(self):
        post = super(PostDetailsView, self).get_object()
        return post

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailsView, self).get_context_data(*args, **kwargs)
        try:
            context['next_post'] = self.object.get_next_by_created_date(status='published')
        except Post.DoesNotExist:
            context['next_post'] = None
        try:
            context['previous_post'] = self.object.get_previous_by_created_date(status='published')
        except Post.DoesNotExist:
            context['previous_post'] = None
        return context
