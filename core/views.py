from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CalendarioForm
from .models import Calendario


class CalendarioCreate(SuccessMessageMixin, CreateView):
    form_class = CalendarioForm
    template_name = 'core/calendario_form.html'
    success_url = reverse_lazy('calendario:calendarios')
    success_message = 'Calendario %(ano)s/%(semestre)s criado com sucesso'

class CalendarioUpdate(SuccessMessageMixin, UpdateView):
    model = Calendario
    form_class = CalendarioForm
    template_name = 'core/calendario_form.html'
    success_url = reverse_lazy('calendario:calendarios')
    success_message = 'Calendario %(ano)s/%(semestre)s editado com sucesso'

class CalendarioDelete(DeleteView):
    model = Calendario
    success_url = reverse_lazy('calendario:calendarios')
    success_message = 'Calendario deletado com sucesso'

    def delete(self, request, *args, **kwargs):
        """Mensagem  de sucesso ao deletar"""
        super(CalendarioDelete, self).delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return redirect(reverse_lazy('calendario:calendarios'))

class CalendarioDetailView(generic.DetailView):
    model = Calendario

class CalendarioListView(generic.ListView): # pylint: disable=too-many-ancestors
    """Generic class-based view for a list of calendarios."""
    model = Calendario
    paginate_by = 10
