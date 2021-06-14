from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
#from .models import Patient, Room, Client
from .models import *
#from django import template TODO

#from extra_views import CreateWithInlinesView, InlineFormSet

# unused
def home(request):
    context = {
            'patients': Patient.objects.all()
            }
    return render(request, 'database/home.html', context)

def about(request):
    return render(request, 'database/about.html')

class PatientListView(ListView):
    model = Patient
    #template_name = 'database/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'patients'
    ordering = ['last_name']

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    """
    total_medicine_price = 0.0
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context['medicine
        """

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    fields = '__all__'

    #fields = ['first_name', 'last_name', 'birth_date', 'diseases', 'is_active',\
    #        'room', 'client', 'email']

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = '__all__'

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = '/'

class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'
    ordering = ['number']

class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room

    """
    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        context['patients'] = Patient.objects.all().filter(room = 1)
        return context
        """

    """
    context = {
            'patients': Room.objects.all()
            }
            """
    #patients = Patient.objects.all().filter(room = model.number)

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = '__all__'

class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = '__all__'

class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    success_url = '/'

class ClientListView(ListView):
    model = Client
    context_object_name = 'clients'
    ordering = ['last_name']

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = '/'

class MedicineListView(ListView):
    model = Medicine
    context_object_name = 'medicines'
    ordering = ['name']

class MedicineDetailView(LoginRequiredMixin, DetailView):
    model = Medicine

class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    fields = '__all__'

class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicine
    fields = '__all__'

class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine
    success_url = '/'

""" TODO
register = template.Library()
@register.simple_tag
def update_variable(value):
    return value
    """
