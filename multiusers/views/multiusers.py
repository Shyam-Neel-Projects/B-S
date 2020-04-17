from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponse


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
            return redirect('customer:homey')
        elif request.user.is_wholesaler:
            return redirect('wholesaler:WProduct_list')
        else:
        	return redirect('pharmacist:pharmapp')
    return render(request, 'multiusers/home.html')
