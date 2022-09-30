# common
from django.urls import path

from petstagram.common.views import index

urlpatterns = (
    # http://127.0.0.1:8000/
    path('', index, name='index'),
)
