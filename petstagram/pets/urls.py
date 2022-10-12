# pets
from django.urls import path, include

from petstagram.pets.views import add_pet, delete_pet, details_pet, edit_pet

urlpatterns = (
    # http://127.0.0.1:8000/pets/add/
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        # http://127.0.0.1:8000/pets/daniel/pet/maxi/delete/
        path('delete/', delete_pet, name='delete pet'),
        # http://127.0.0.1:8000/pets/daniel/pet/maxi/
        path('', details_pet, name='details pet'),
        # http://127.0.0.1:8000/pets/daniel/pet/maxi/edit/
        path('edit/', edit_pet, name='edit pet'),
    ])),
)
