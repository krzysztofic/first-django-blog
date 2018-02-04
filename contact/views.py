from django.views.generic import DetailView, FormView
from .models import Message
from .forms import MessageForm

# class MesssageDetailView(DetailView):
#     model = Message

class MessageAddView(FormView):
    form_class = MessageForm
    template_name = 'contact/blog_message.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(MessageAddView, self).form_valid(form)
