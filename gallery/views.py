from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.db.models import F
from .models import Gallery

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery_list.html'
    context_object_name = 'gallery'

class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery_detail.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         model_entry = Gallery.objects.filter(slug=self.kwargs.get('slug'))
         model_entry.update(count=F('count') +1)
         context["time"] = timezone.now() 
         return context

# Create your views here.
