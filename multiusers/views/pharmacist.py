from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.http import HttpResponse

from ..decorators import pharmacist_required
from ..forms import PharmacistSignUpForm
from ..models import User, Category, Product, ApprovImg


class PharmacistSignUpView(CreateView):
    model = User
    form_class = PharmacistSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pharmacist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponse("Hello pharmacist")

@login_required
@pharmacist_required
def homey(request):
    return HttpResponse("Hello")


@login_required
@pharmacist_required
def pharmapp(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    wproducts = Product.objects.filter()
    f = ApprovImg.objects.all()
    #f = ApprovImg.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        wproducts = Product.objects.filter()
        #f = approveform(request.POST,request.FILES)
        
        #f.save()
       # pho = approv.objects.all()
        
    context = {
        'category': category,
        'categories': categories,
        'wproducts': wproducts,
        'f' : f
    }
    return render(request, 'multiusers/pharmacist/p_w.html', context)