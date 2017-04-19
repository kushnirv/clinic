from django.views.generic import ListView
from .models import Doctor, Appointment
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy as reverse
from django.shortcuts import get_object_or_404


# Create your views here.

class DoctorListView(ListView):
    queryset = Doctor.objects.all()\
        .select_related('specialization')\
        .order_by('specialization__name', 'full_name')

    def get_context_data(self, **kwargs):
        context = super(DoctorListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query', '')
        return context

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        if query:
            self.queryset = self.queryset.filter(full_name__icontains=query)
        return self.queryset


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ('full_name', 'doctor', 'date')
    success_url = reverse('index')

    def get_context_data(self, **kwargs):
        context = super(AppointmentCreateView, self).get_context_data(**kwargs)
        context['name_doctor'] = get_object_or_404(
            Doctor.objects,
            pk=self.kwargs['pk']
        )
        return context

    def get_form_kwargs(self):
        form_kwargs = super(AppointmentCreateView, self).get_form_kwargs()
        if 'data' in form_kwargs:
            data = form_kwargs['data'].copy()
            data['doctor'] = self.kwargs['pk']
            form_kwargs['data'] = data
        return form_kwargs
