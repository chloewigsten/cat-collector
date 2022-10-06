from ast import Delete
from audioop import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Breed, Characteristics, Color, Personality
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.
class Home(TemplateView): 
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personality'] = Personality.objects.all()
        return context

class About(TemplateView):
    template_name = 'about.html'

class Cat:
    def __init__(self, breed, image, details):
        self.breed = breed
        self.image = image
        self.details = details 

class CatBreedList(TemplateView):
    template_name = "cat-breeds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        breed = self.request.GET.get("breed")
        # If a query exists we will filter by name 
        if breed != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["breeds"] = Breed.objects.filter(breed__icontains=breed)
        else:
            context["breeds"] = Breed.objects.all()
        return context

class BreedsCreate(CreateView):
    model = Breed
    fields = ['breed', 'image', 'details']
    template_name = 'breeds_create.html'
    def get_success_url(self):
        return reverse('create-breed', kwargs={'pk': self.object.pk})


class BreedDetails(DetailView):
    model = Breed
    template_name= 'breed_detail.html'

class BreedUpdate(UpdateView):
    model = Breed
    fields = ['breed', 'image', 'details']
    template_name = 'breed_update.html'
    def get_success_url(self): 
        return reverse('breed detail', kwargs={'pk': self.object.pk})

class BreedDelete(DeleteView):
    model = Breed
    template_name= 'breed_delete.html'
    success_url = '/cat-breeds'


class ColorCreate(View):
    def post(self, request, pk):
        coat = request.POST.get("color")
        pattern = request.POST.get("pattern")
        colors = Breed.objects.get(pk=pk)
        Color.objects.create(coat=coat, pattern=pattern, colors=colors)
        return redirect('breed_detail', pk=pk)

class CharacteristicCreate(View):
    def post(self, request, pk):
        traits = request.POST.get("traits")
        temperament = request.POST.get("temperament")
        characteristics = Breed.objects.get(pk=pk)
        Characteristics.objects.create(traits=traits, temperament=temperament, characteristics=characteristics)
        return redirect('breed_detail', pk=pk)

class PersonalityCharacteristics(View):
    def get(self, request, pk, characteristic_pk):
        assoc = request.GET.get('assoc')
        if assoc == "remove":
            Personality.objects.get(pk=pk).characteristics.remove(characteristic_pk)
        if assoc == "add":
            Personality.objects.get(pk=pk).characteristics.add(characteristic_pk)
        return redirect('home')