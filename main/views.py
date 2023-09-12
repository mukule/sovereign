from django.shortcuts import render, redirect, get_object_or_404
from .models import Hero
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    try:
        hero = get_object_or_404(Hero)
    except Hero.DoesNotExist:
        hero = None  # Set hero to None if no matching object is found

    events = Event.objects.all()  # Retrieve all events
    return render(request, 'main/index.html', {'hero': hero, 'events': events})

def dashboard(request):
    return render(request, 'main/dashboard.html')

def hero(request):
    # Check if a hero instance already exists
    hero = Hero.objects.first()

    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES, instance=hero)

        if form.is_valid():
            form.save()
            messages.success(request, 'Hero information updated successfully.')
            return redirect('main:dashboard')
        else:
            messages.error(request, 'There was an error in the form submission. Please check the form.')

    else:
        form = HeroForm(instance=hero)

    return render(request, 'main/hero_form.html', {'form': form})

def create_senior(request):
    if request.method == 'POST':
        form = SeniorForm(request.POST, request.FILES)

        if form.is_valid():
            # Check if an image file was provided, if not, set it to the default value
            if not form.cleaned_data['profile_pic']:
                form.cleaned_data['profile_pic'] = 'seniors/default/user.jpg'

            form.save()
            messages.success(request, 'Senior profile created successfully.')
            return redirect('main:seniors')
        else:
            messages.error(request, 'Error creating senior profile. Please check the form.')
    else:
        form = SeniorForm(initial={'profile_pic': 'seniors/default/user.jpg'})  # Set the default image path

    return render(request, 'main/create_senior.html', {'form': form})



def edit_senior(request, senior_id):
    senior = Senior.objects.get(pk=senior_id)

    if request.method == 'POST':
        form = SeniorForm(request.POST, request.FILES, instance=senior)

        if form.is_valid():
            form.save()
            messages.success(request, 'Senior profile updated successfully.')
            return redirect('main:seniors')
        else:
            messages.error(request, 'Error updating senior profile. Please check the form.')

    else:
        form = SeniorForm(instance=senior)

    return render(request, 'main/edit_senior.html', {'form': form})


def delete_senior(request, senior_id):
    senior = Senior.objects.get(pk=senior_id)
    senior.delete()
    messages.success(request, 'Senior profile deleted successfully.')
    return redirect('main:seniors')

def seniors(request):
    seniors = Senior.objects.all()
    return render(request, 'main/seniors.html', {'seniors': seniors})


def create_company(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:companies')
    else:
        form = CompanyProfileForm()
    return render(request, 'main/create_company.html', {'form': form})

def edit_company_profile(request, pk):
    company_profile = get_object_or_404(CompanyProfile, pk=pk)
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES, instance=company_profile)
        if form.is_valid():
            form.save()
            return redirect('main:companies')
    else:
        form = CompanyProfileForm(instance=company_profile)
    return render(request, 'main/edit.html', {'form': form, 'company_profile': company_profile})

def delete_company_profile(request, pk):
    company_profile = get_object_or_404(CompanyProfile, pk=pk)
    messages.success(request, 'The company was deleted succesfully')
    company_profile.delete()
    return redirect('main:companies')

def company_profile_detail(request, pk):
    company_profile = get_object_or_404(CompanyProfile, pk=pk)
    return render(request, 'main/company.html', {'company_profile': company_profile})

def companies(request):
    company_profiles = CompanyProfile.objects.all()
    return render(request, 'main/companies.html', {'companies': company_profiles})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Event Added succesfully')
            return redirect('main:events')
    else:
        form = EventForm()
    return render(request, 'main/create_event.html', {'form': form})

def events(request):
    events = Event.objects.all()
    return render(request, 'main/events.html', {'events': events})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            messages.success(request, 'Event Updated succesfully')
            return redirect('main:events')
    else:
        form = EventForm(instance=event)

    return render(request, 'main/edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('main:events')