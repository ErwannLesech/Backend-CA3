# import necessary modules
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Motorcycle
from .forms import CreateNewMotorcycle
from django.shortcuts import redirect

# Hacking security

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse

# view function for displaying list of latest motorcycles
def index(request):
    # retrieve the latest motorcycles
    latest_motorcycle_list = Motorcycle.objects.order_by('-pub_date')[:5]
    context = {'latest_motorcycle_list': latest_motorcycle_list}
    # render the index template with context
    return render(request, 'garage/index.html', context)

# view function for displaying details of a motorcycle
def description(request, motorcycle_id):
    # get the motorcycle with the specified ID or return a 404 error
    motorcycle = get_object_or_404(Motorcycle, pk=motorcycle_id)
    # render the description template with motorcycle object as context
    return render(request, 'garage/description.html', {'motorcycle': motorcycle})

# view function for creating a new motorcycle
def create(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CreateNewMotorcycle(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data["motorcycle_text"]
            description = form.cleaned_data["motorcycle_description"]
            brand = form.cleaned_data["motorcycle_brand"]
            time = form.cleaned_data["pub_date"]
            # create a new motorcycle object and save it to the database
            Motorcycle.objects.create(motorcycle_text=name, motorcycle_brand=brand, motorcycle_description=description, pub_date=time)
            # redirect to the index page
            try:
                # construct the URL for the motorcycle's detail page
                url = '../'
                # redirect to the motorcycle's detail page
                return redirect(url)
            except ValidationError:
                # if the URL is invalid, return a 404 error
                return HttpResponse(status=404)
    else:
        # if a GET request is made, create a blank form
        form = CreateNewMotorcycle()
    # render the create template with form object as context
    return render(request, 'garage/create.html', {'form': form})

# view function for updating a motorcycle
def update(request, motorcycle_id):
    # get the motorcycle object to be updated
    motorcycle = Motorcycle.objects.get(pk=motorcycle_id)
    # create a form instance and populate it with the motorcycle object's data
    form = CreateNewMotorcycle(instance=motorcycle)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CreateNewMotorcycle(request.POST, instance=motorcycle)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to the index page
            return redirect('../')
    context = {'form': form}
    # render the update template with form object as context
    return render(request, 'garage/update.html', context)

# view function for deleting a motorcycle
def delete(request, motorcycle_id):
    # get the motorcycle object to be deleted
    motorcycle = Motorcycle.objects.get(pk=motorcycle_id)
    if request.method == "POST":
        # delete the motorcycle object from the database
        motorcycle.delete()
        # redirect to the index page
        return redirect('../../')
    # render the delete template with motorcycle object as context
    return render(request, 'garage/delete.html', {'motorcycle': motorcycle})