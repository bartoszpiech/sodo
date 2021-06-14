from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Patient, Room, Client

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
