from django.views.generic import TemplateView
from main.models import BlogPost

'''
Esta es la vista principal
'''

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.order_by('-pk')[:3]
        return context