from django.urls import path
from .views import sign_up, sign_in, sign_out, UpdateUser

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path('user/_update/', UpdateUser.as_view(), name='update_user'),
]