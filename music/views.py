from django.views import generic
from . models import Album

class IndexView(generic.ListView):
    context_object_name = 'all_albums'
    template_name = "music/index.html"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'


