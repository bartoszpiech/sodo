from django.urls import path
"""
from .views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView
from .views import RoomListView, RoomDetailView, RoomCreateView, RoomUpdateView, RoomDeleteView
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView
"""
from .views import *
from . import views

urlpatterns = [
        path('', PatientListView.as_view(), name = 'database-home'),
        path('about/', views.about, name = 'database-about'),

        path('patient/', PatientListView.as_view(), name = 'database-home'),
        path('patient/<int:pk>/', PatientDetailView.as_view(), \
                name = 'database-patient-detail'),
        path('patient/new/', PatientCreateView.as_view(), \
                name = 'database-patient-create'),
        path('patient/<int:pk>/update/', PatientUpdateView.as_view(), \
                name = 'database-patient-update'),
        path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), \
                name = 'database-patient-delete'),

        path('room/', RoomListView.as_view(), name = 'database-room'),
        path('room/<int:pk>/', RoomDetailView.as_view(), \
                name = 'database-room-detail'),
        path('room/new/', RoomCreateView.as_view(), \
                name = 'database-room-create'),
        path('room/<int:pk>/update/', RoomUpdateView.as_view(), \
                name = 'database-room-update'),
        path('room/<int:pk>/delete/', RoomDeleteView.as_view(), \
                name = 'database-room-delete'),

        path('client/', ClientListView.as_view(), name = 'database-client'),
        path('client/<int:pk>/', ClientDetailView.as_view(), \
                name = 'database-client-detail'),
        path('client/new/', ClientCreateView.as_view(), \
                name = 'database-client-create'),
        path('client/<int:pk>/update/', ClientUpdateView.as_view(), \
                name = 'database-client-update'),
        path('client/<int:pk>/delete/', ClientDeleteView.as_view(), \
                name = 'database-client-delete'),

        path('medicine/', MedicineListView.as_view(), name = 'database-medicine'),
        path('medicine/<int:pk>/', MedicineDetailView.as_view(), \
                name = 'database-medicine-detail'),
        path('medicine/new/', MedicineCreateView.as_view(), \
                name = 'database-medicine-create'),
        path('medicine/<int:pk>/update/', MedicineUpdateView.as_view(), \
                name = 'database-medicine-update'),
        path('medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), \
                name = 'database-medicine-delete'),
        ]
