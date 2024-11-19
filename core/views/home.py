from django.views.generic import ListView
from account.models import CustomUser



class HomeView(ListView):
    template_name = 'home/home.html'
    model = CustomUser
    context_object_name = 'users'