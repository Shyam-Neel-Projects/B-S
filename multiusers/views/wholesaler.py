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

from ..decorators import wholesaler_required
from ..forms import WholesalerSignUpForm, ApproveImgForm
from ..models import User, Category, Product
from django.http import HttpResponse

class WholesalerSignUpView(CreateView):
    model = User
    form_class = WholesalerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'wholesaler'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponse("Hello wholesaler")


@login_required
@wholesaler_required
def homey(request):
    return HttpResponse("Hello")


@login_required
@wholesaler_required
def WProduct_list(request, category_slug=None):
    
    category = None
    categories = Category.objects.all()
    wproducts = Product.objects.filter()
    
        # f = approv(photo=request.FILES['photo'])
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        wproducts = Product.objects.filter()
        print('error bc')
   
    if request.method == 'POST':
        form = ApproveImgForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponse('Success')
    else:
        form = ApproveImgForm
                
    context = {
        'category': category,
        'categories': categories,
        'wproducts': wproducts,
        'form': form,
    }
    return render(request, 'multiusers/wholesaler/w_p.html', context)