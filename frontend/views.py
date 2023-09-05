from django.shortcuts import render, get_object_or_404
from main.models import *

# Create your views here.
def seniors(request):
    seniors = Senior.objects.all()
    return render(request, 'frontend/seniors.html', {'seniors': seniors})

def senior_detail(request, pk):
    senior = get_object_or_404(Senior, pk=pk)
    return render(request, 'frontend/senior_detail.html', {'senior': senior})


def companies(request):
    company_profiles = CompanyProfile.objects.all()
    return render(request, 'frontend/companies.html', {'companies': company_profiles})

def company_detail(request, company_id):
    company = get_object_or_404(CompanyProfile, pk=company_id)
    events = Event.objects.filter(company=company)
    return render(request, 'frontend/company_detail.html', {'company': company, 'events': events})

def events(request):
    events = Event.objects.all()
    return render(request, 'frontend/events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'frontend/event_detail.html', {'event': event})