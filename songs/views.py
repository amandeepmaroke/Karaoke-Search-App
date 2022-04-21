from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Song
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Song
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Song.objects.filter(Q(artist__icontains=query) | Q(title__icontains=query))
        return object_list

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    
