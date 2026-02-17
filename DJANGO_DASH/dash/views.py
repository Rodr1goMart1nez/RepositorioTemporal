from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import WalleBpm
from .forms import WalleBpmForm

class WalleListView(ListView):
    model = WalleBpm
    template_name = 'dash/walle_list.html'
    context_object_name = 'walle_list'
    paginate_by = 10 # Activar paginación

    def get_queryset(self):
        queryset = super().get_queryset()
        
        
        # Búsquedas específicas
        q_process_id = self.request.GET.get('q_process_id')
        if q_process_id:
            queryset = queryset.filter(process_id=q_process_id)
            
        q_nro_doc = self.request.GET.get('q_nro_doc')
        if q_nro_doc:
            queryset = queryset.filter(nro_doc__icontains=q_nro_doc)

        q_nro_cliente = self.request.GET.get('q_nro_cliente')
        if q_nro_cliente:
            queryset = queryset.filter(nro_cliente__icontains=q_nro_cliente)

        q_status_id = self.request.GET.get('q_status_id')
        if q_status_id:
            queryset = queryset.filter(status_id=q_status_id)

        return queryset.order_by('-fecha_hora') # Ordenar por fecha descendente por defecto

    def get(self, request, *args, **kwargs):
        if request.GET.get('export') == 'excel':
            return self.export_to_excel(request)
        return super().get(request, *args, **kwargs)

    def export_to_excel(self, request):
        import openpyxl
        from django.http import HttpResponse

        queryset = self.get_queryset()
        
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=walle_procesos.xlsx'

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Procesos Walle"

        # Encabezados
        columns = [
            'Process ID', 'Nombre', 'Nro. Doc', 'Nro. Cliente', 'Impacto', 
            'Status ID', 'Priority ID', 'Operación', 'Op. Desc', 'Fecha y Hora', 
            'Comentario', 'Gerente', 'Ingresante'
        ]
        ws.append(columns)

        # Datos
        for obj in queryset:
            # Eliminar zona horaria para compatibilidad con Excel si es necesario, 
            # o dejar que openpyxl lo maneje (a veces da warnings con tz-aware datetimes)
            fecha_hora = obj.fecha_hora.replace(tzinfo=None) if obj.fecha_hora else None
            
            row = [
                obj.process_id,
                obj.nombre,
                obj.nro_doc,
                obj.nro_cliente,
                obj.impacto,
                obj.status_id,
                obj.priority_id,
                obj.operacion,
                obj.op_desc,
                fecha_hora,
                obj.comentario,
                obj.gerente,
                obj.ingresante
            ]
            ws.append(row)

        wb.save(response)
        return response


class WalleUpdateView(SuccessMessageMixin, UpdateView):
    model = WalleBpm
    form_class = WalleBpmForm
    template_name = 'dash/walle_detail.html'
    context_object_name = 'walle'
    pk_url_kwarg = 'process_id'
    success_message = "¡Los cambios se han guardado correctamente!"

    def get_success_url(self):
        return reverse_lazy('walle_detail', kwargs={'process_id': self.object.process_id})

class WalleCreateView(SuccessMessageMixin, CreateView):
    model = WalleBpm
    form_class = WalleBpmForm
    template_name = 'dash/walle_detail.html'
    success_message = "¡El nuevo proceso se ha creado correctamente!"
    
    def get_success_url(self):
        return reverse_lazy('walle_detail', kwargs={'process_id': self.object.process_id})