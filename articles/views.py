from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.view.generic.list import ListView
from django.utils import timezone
from django.db.models import F
from .models import Articles


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Articles.objects.all()[:3]
        #href = "{% url 'articles:article-detail' slug=latest_articles.slug%}"
        #the above will reference the 
        return context

class ArticleDetailView(DetailView):
     
     #queryset = Articles.objects.all() #alternative to below for more granula operations
     model = Articles
     template_name = 'article-detailview.html'
     context_object_name = 'article'

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         model_entry = Articles.objects.filter(slug=self.kwargs.get('slug'))
         model_entry.update(count=F('count') +1)
         context["time"] = timezone.now() 
         return context

class ArticleListView(ListView):
    model = Articles
    context_object_name = 'article-list'
    template_name='article-listview.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        snippet = f"{Articles.objects.filter(content=self.kwargs.get('content'))[:100]}..."
        context["snippet"] = snippet
        context['article'] = Articles.objects.all()
        #href = "{% url 'articles:article-detail' slug=article.slug%}"
        return context
    
class GenreListView(ListView):
    model = Articles
    context_object_name = 'article-list'
    template_name='article-listview.html'
    paginate_by = 2 

    def get_queryset(self,*args, **kwargs):
       return Articles.objects.filter(genre__icontains=self.kwargs.get('genre'))
    