from django.urls import path
from . import views



app_name = 'frontend'
urlpatterns = [
    path("seniors", views.seniors, name="seniors"),
    path("companies", views.companies, name="companies"),
    path("events", views.events, name="events"),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('seniors/<int:pk>/', views.senior_detail, name='senior_detail'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
]