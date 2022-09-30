# accounts
from django.urls import path, include

from petstagram.accounts.views import login_user, register_user, details_user, edit_user, delete_user

urlpatterns = (
    # http://127.0.0.1:8000/accounts/login/
    path('login/', login_user, name='login user'),
    # http://127.0.0.1:8000/accounts/register/
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        # http://127.0.0.1:8000/accounts/profile/1/
        path('', details_user, name='details user'),
        # http://127.0.0.1:8000/accounts/profile/1/edit/
        path('edit/', edit_user, name='edit user'),
        # http://127.0.0.1:8000/accounts/profile/1/delete/
        path('delete/', delete_user, name='deletes user'),
    ])),
)
