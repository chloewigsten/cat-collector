from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('cat-breeds/', views.CatBreedList.as_view(), name='cat-breeds'),
    path('cat-breeds/new/', views.BreedsCreate.as_view(), name='breed-create'),
    path('cat-breeds/<int:pk>/', views.BreedDetails.as_view(), name='breed_detail'),
    path('cat-breeds/<int:pk>/update', views.BreedUpdate.as_view(), name='breed-update'),
    path('cat-breeds/<int:pk>/delete', views.BreedDelete.as_view(), name='breed-delete'),
    path('cat-breeds/<int:pk>/colors/new', views.ColorCreate.as_view(), name='color_create'),
    path('cat-breeds/<int:pk>/characteristics/new', views.CharacteristicCreate.as_view(), name='characteristic_create'),
    path('personaility/<int:pk>/characteristics/<int:characteristic_pk>/', views.PersonalityCharacteristics.as_view(), name='personality_characteristics')
]

