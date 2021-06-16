from django.views.generic.base import TemplateView
from articles.models import Articles

class HomePageView(TemplateView):
    
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Articles.objects.all()[:3]
        #href = "{% url 'articles:article-detail' slug=latest_articles.slug%}"
        #the above will reference the 
        return context

class ServicesPageView(TemplateView):
    template_name = 'services.html'