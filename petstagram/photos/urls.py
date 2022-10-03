# photos
from django.urls import path, include

from petstagram.photos.views import add_photo, details_photo, edit_photo

urlpatterns = (
    # http://127.0.0.1:8000/photos/add/
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        # http://127.0.0.1:8000/photos/1/
        path('', details_photo, name='details photo'),
        # http://127.0.0.1:8000/photos/1/edit/
        path('edit/', edit_photo, name='edit photo')
    ])),
)
