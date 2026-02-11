from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from .models import WalleBpm
from .forms import WalleBpmForm

class WalleListView(ListView):
    model = WalleBpm
    template_name = 'dash/walle_list.html'
    context_object_name = 'walle_list'
    paginate_by = 10 # Activar paginación

class WalleUpdateView(UpdateView):
    model = WalleBpm
    form_class = WalleBpmForm
    template_name = 'dash/walle_detail.html'
    context_object_name = 'walle'
    pk_url_kwarg = 'process_id'

    def get_success_url(self):
        return reverse_lazy('walle_detail', kwargs={'process_id': self.object.process_id})

class WalleCreateView(CreateView):
    model = WalleBpm
    form_class = WalleBpmForm
    template_name = 'dash/walle_detail.html'
    
    def get_success_url(self):
        return reverse_lazy('walle_detail', kwargs={'process_id': self.object.process_id})