from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django_registration.backends.activation.views import RegistrationView

# Create your views here.


@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")



