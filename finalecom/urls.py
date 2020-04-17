from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

from multiusers.views import multiusers, customer, wholesaler, pharmacist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('multiusers.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', multiusers.SignUpView.as_view(), name='signup'),
    path('accounts/signup/customer/', customer.CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/signup/pharmacist/', pharmacist.PharmacistSignUpView.as_view(), name='pharmacist_signup'),
    path('accounts/signup/wholesaler/', wholesaler.WholesalerSignUpView.as_view(), name='wholesaler_signup'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
