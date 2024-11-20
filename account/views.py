from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.views.generic import UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from account.models import CustomUser
import json

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'authentication/flows/basic/sign-in.html', {'form': form})

@login_required
def sign_out(request):
    logout(request)
    return redirect('home')


class UpdateUser(UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name')

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, id=self.request.POST.get('val', self.request.GET.get('val')))

    # def get(self, request, *args, **kwargs):
    #     dataobj = self.user
    #     company = self.company
    #     form = self.form

    # def post(self, request, *args, **kwargs):
    #     linked_orgaccess = self.linked_orgaccess
    #     dataobj = self.user
    #     company = self.company
    #     form = self.form
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.last_updated_by = request.user
    #         user.last_updated_on = datetime.now(pytz.UTC)

    def render_to_response(self, context, *args, **kwargs):
        if self.request.method == 'POST':
            pass
        elif self.request.method == 'GET':
            html = render_to_string('partials/modals/_update_user.html', context)
            return HttpResponse(json.dumps(html), content_type="application/json")